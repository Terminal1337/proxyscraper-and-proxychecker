import os
import requests
import sys
import threading
import time

PyVer = str(sys.version)

def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

cls()

def checker(PROXY,url):
    try:
        s = requests.sion()
        s.proxies = {'http': PROXY}
        s.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

        respone = s.get(url,timeout = 5,proxies={'http':PROXY})
        if respone.status_code == 200:
            print(PROXY + '   GOOD')
            with open('proxies.txt','a') as xX:
                xX.write(PROXY + '\n')
        else:
            print(PROXY + "  BAD")

    except:
        print(PROXY + "  BAD")

def main():
    try:
        if '3' in PyVer:
            try:
                proxy = input("[+] Name of Proxy List: ")
            except:
                print("[-]Error: Enter your Proxy List")
                sys.exit()
        elif '2' in PyVer:
            try:
                proxy = input("[+]Name of the Proxy List: ")
            except:
                print('[-]Eror: Enter your proxy list: ')
                sys.exit()
        else:
            print("Python Version is unknown")
    except: 
        pass
        sys.exit()
    with open(proxy,'r') as x:
        proxyy = x.read().splitlines()
    thread = []

    for proxy in proxyy:
        t = threading.Thread(target = checker,args=(proxy,'https://duckduckgo.com'))
        t.start()
        thread.append(t)
        time.sleep(0.1)
    for i in thread:
        i.join()
main()
                
        
