import argparse, threading, requests
from random_word import RandomWords
rand = RandomWords()

def check_from_file(file):
    for name in open(file, "r").read().splitlines():
        r = requests.get(f"https://github.com/{name}")
        if r.status_code == 404:
            print(f"[+] Available : {name}")

def gen_random():
    while True:
        name = rand.get_random_word()
        if name == None:
            pass
        elif name.isalnum() == False:
            pass
        else:
            r = requests.get(f"https://github.com/{name}") 
            if r.status_code == 404:
                print(f"[+] Available : {name}")


parser = argparse.ArgumentParser(description='Github username checker')
parser.add_argument("-r", "--random", help="Specify amount of threads")
parser.add_argument("-f", "--file", help="Specifcy a file location")
args = parser.parse_args()
if args.file == None and args.random == None:
    parser.print_help()
elif args.file:
    check_from_file(file=args.file)
elif args.random:
    threads = []
    for i in range(int(args.random)):
        proc = threading.Thread(target=gen_random)
        proc.start()
        threads.append(proc)
