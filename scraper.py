import requests

proxy_type = input("Enter the Type of Proxy(socks4/socks4/http): ")
proxy_timeout = input("Enter The Proxy Timeout(ms): ")
proxy_anonymity = input("Enter the Proxy Anonymity(elite/transparent/anonymous/all): ")
response = requests.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={proxy_type}&timeout={proxy_timeout}&country=all&ssl=all&anonymity={proxy_anonymity}")

proxy= response.text

file = open("proxies.txt",'w')
file.write(proxy)
file.close()
