import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp_path ="hosts.txt"
redirect_address = "127.0.0.1"
blocked_websites = ["www.youtube.com", "youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working")
        with open(hosts_temp_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect_address + " " + website + "\n")

    else:
        print("Free time")
    
    time.sleep(2)
