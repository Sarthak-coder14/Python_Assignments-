import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage
from datetime import datetime


EXCLUDE_EXT = [".tmp", ".log", ".exe"]



def CreateLog():
    os.makedirs("Logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join("Logs", f"Log_{timestamp}.txt")

def WriteLog(logfile, message):
    with open(logfile, "a") as f:
        f.write(message + "\n")


def calculate_hash(path):
    hobj = hashlib.md5()
    with open(path,"rb") as f:
        while chunk := f.read(1024):
            hobj.update(chunk)
    return hobj.hexdigest()


def BackupFiles(Source, Destination, logfile):
    copied_files = []
    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:

            if any(file.endswith(ext) for ext in EXCLUDE_EXT):
                continue

            src_path = os.path.join(root,file)
            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            try:
                if((not os.path.exists(dest_path)) or
                   (calculate_hash(src_path) != calculate_hash(dest_path))):

                    shutil.copy2(src_path, dest_path)
                    copied_files.append(relative)

            except Exception as e:
                WriteLog(logfile, f"Error copying {file} : {e}")

    return copied_files

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    with zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED) as zobj:
        for root, dirs, files in os.walk(folder):
            for file in files:
                full_path = os.path.join(root,file)
                relative = os.path.relpath(full_path,folder)
                zobj.write(full_path,relative)

    return zip_name


def SendEmail(logfile, zipfile_name):

    sender = "your_email@gmail.com"
    password = "your_app_password"


    msg = EmailMessage()
    msg['Subject'] = "Backup Completed"
    msg['From'] = sender
    msg['To'] = "receiver@gmail.com"

    msg.set_content("Backup completed successfully.\nLog and Zip attached.")

    for file in [logfile, zipfile_name]:
        with open(file, "rb") as f:
            msg.add_attachment(f.read(),
                               maintype="application",
                               subtype="octet-stream",
                               filename=os.path.basename(file))

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender,password)
        smtp.send_message(msg)


def UpdateHistory(zipfile_name, filecount):
    size = os.path.getsize(zipfile_name)
    with open("history.txt","a") as f:
        f.write(f"{datetime.now()} | Files: {filecount} | ZipSize: {size}\n")

def ShowHistory():
    if os.path.exists("history.txt"):
        with open("history.txt") as f:
            print(f.read())
    else:
        print("No history found.")


def RestoreBackup(zipname, destination):
    with zipfile.ZipFile(zipname,'r') as z:
        z.extractall(destination)
    print("Restore completed.")


def MarvellousDataShieldStart(Source="Data"):

    logfile = CreateLog()
    WriteLog(logfile, "Backup started at : " + str(datetime.now()))

    BackupName = "MarvellousBackup"

    files = BackupFiles(Source, BackupName, logfile)
    zip_file = make_zip(BackupName)

    WriteLog(logfile, f"Files copied : {len(files)}")
    WriteLog(logfile, f"Zip file : {zip_file}")

    UpdateHistory(zip_file, len(files))



def main():

    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        ShowHistory()

    elif len(sys.argv) == 4 and sys.argv[1] == "--restore":
        RestoreBackup(sys.argv[2], sys.argv[3])

    elif len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(
            MarvellousDataShieldStart, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Usage:")
        print("python Script.py 5 Data")
        print("python Script.py --restore zipfile destination")
        print("python Script.py --history")

if __name__ == "__main__":
    main()
