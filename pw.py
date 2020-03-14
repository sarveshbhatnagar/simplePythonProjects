#! python3
# pw.py - An insecure password manager
import pickle

def saveFile(obj,filename):
    with open(filename,'wb') as f:
        pickle.dump(obj, f)

def readFile(filename):
    with open(filename,'rb') as f:
        x = pickle.loads(f.read())
    return x

try:
    PASSWORDS = readFile('passwords.txt')
except Exception:
    PASSWORDS = dict()

import sys,pyperclip

if(len(sys.argv) < 2):
    print('Usage: python pw.py [acccount] - copy account password')
    sys.exit()

account = sys.argv[1]

if(len(sys.argv) > 2):
    PASSWORDS[account] = sys.argv[2]
else:
    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for '+ account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)

saveFile(PASSWORDS,'passwords.txt')
