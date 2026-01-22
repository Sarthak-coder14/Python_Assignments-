def checkvowel(ch):
    if ch.lower() in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

def main():
    ch = input("Enter character: ")
    print(checkvowel(ch))
    
if __name__=="__main__":

    main()
