import psutil
import os
import sys
import time
import schedule
import smtplib
from email.message import EmailMessage
from datetime import datetime


def CreateLogFolder(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created succesfully")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    logfile = os.path.join(FolderName, f"Log_{timestamp}.log")


    try:
        fobj = open(logfile, "w")

        fobj.write("-"*80 + "\n")
        fobj.write("Platform Surveillance System Log\n")
        fobj.write("Timestamp : " + str(datetime.now()) + "\n")
        fobj.write("-"*80 + "\n\n")

        process_list = []

        for proc in psutil.process_iter(['pid','name','memory_info','num_threads','open_files','cpu_percent']):
            try:
                info = proc.info

                pid = info['pid']
                name = info['name']
                cpu = proc.cpu_percent(interval=0.1)
                threads = info['num_threads']


                rss = info['memory_info'].rss
                vms = info['memory_info'].vms
                mem_percent = proc.memory_percent()

                try:
                    open_files = len(proc.open_files())
                except:
                    open_files = "Access Denied"

                process_list.append((name, pid, mem_percent))

             
                fobj.write(f"Process Name : {name}\n")
                fobj.write(f"PID          : {pid}\n")
                fobj.write(f"CPU %        : {cpu}\n")
                fobj.write(f"Memory (RSS) : {rss}\n")
                fobj.write(f"Memory (VMS) : {vms}\n")
                fobj.write(f"Memory %     : {mem_percent}\n")
                fobj.write(f"Threads Count: {threads}\n")
                fobj.write(f"Open Files   : {open_files}\n")
                fobj.write(f"Timestamp    : {datetime.now()}\n")
                fobj.write("-"*80 + "\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        fobj.write("\nTop 10 Memory Consuming Processes\n")
        fobj.write("-"*80 + "\n")

        process_list.sort(key=lambda x: x[2], reverse=True)

        for i in process_list[:10]:
            fobj.write(f"{i[0]} (PID:{i[1]}) -> {i[2]} %\n")

        fobj.close()

        return logfile

    except Exception as e:
        print("Error :", e)


def SendEmail(receiver, logfile):

    try:
        sender = "your_email@gmail.com"
        password = "your_app_password"

        msg = EmailMessage()
        msg['Subject'] = "Platform Surveillance Report"
        msg['From'] = sender
        msg['To'] = receiver

        msg.set_content("System Monitoring Report Attached")

        with open(logfile, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(logfile)

        msg.add_attachment(file_data, maintype='application',
                           subtype='octet-stream', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

    except Exception as e:
        print("Email Error :", e)


def PlatformSurveillance(folder_name, receiver):

    logfile = CreateLogFolder(folder_name)

    

    SendEmail(receiver, logfile)

def main():

    Border = "-"*80

    if len(sys.argv) != 4:
        print("Usage : PlatformSurveillance.py LogFolder ReceiverEmail IntervalInMinutes")

    folder = sys.argv[1]
    receiver = sys.argv[2]
    
    print(Border)
    print("Platform Surveillance System Started...")
    print("Log Folder :", folder)
    print("Receiver   :", receiver)
    print("Interval   :", int(sys.argv[3]), "minutes")
    print(Border)

    schedule.every(int(sys.argv[3])).minutes.do(PlatformSurveillance, folder, receiver)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
