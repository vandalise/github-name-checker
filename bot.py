from random_word import RandomWords
rand = RandomWords()
import requests
import threading
import os

def check_random():
    while True:
        try:
            name = rand.get_random_word(hasDictionaryDef="true")
            if name == None:
                pass
            else:
                if name.isalnum() == True:
                    r = requests.get(f"https://github.com/{name}")
                    if r.status_code == 404:
                        print(f"[+] Available : {name}")
                    else:
                        pass
                else:
                    pass
        except:
            pass

def check_from_list(filepath):
    file = open(filepath, "r").read().splitlines()
    for name in file:
        if name.isalnum() == True:
            r = requests.get(f"https://github.com/{name}")
            if r.status_code == 404:
                print(f"[+] Available : {name}")
            else:
                pass

def main():
    print("[1] Check random generated names\n[2] Check names from file")
    try:
        option = int(input("> "))
    except ValueError:
        main()
    if option not in(1, 2):
        main()
    elif option == 1:
        threads = []
        for i in range(10):
            t = threading.Thread(target=check_random)
            threads.append(t)
            t.start()
    elif option == 2:
        filepath = input("File path (ex: names.txt): ")
        if os.path.exists(filepath):
            check_from_list(filepath)
        else:
            main()

main()
