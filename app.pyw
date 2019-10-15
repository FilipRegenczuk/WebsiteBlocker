import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp_path =r"C:\Users\frege\OneDrive\Documents\Python\WebsiteBlocker\hosts"   # used for testing
redirect_address = "127.0.0.1"
blocked_websites = ["www.youtube.com", "youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in blocked_websites:
                if website in content:
                    pass
                else:
                    file.write(redirect_address + " " + website + "\n")

    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()          # create a list of strings
            file.seek(0)                        # return pointer to first line
            for line in content:
                if not any(website in line for website in blocked_websites):
                    file.write(line)
            file.truncate()         # delete previous version

    time.sleep(5)       # refresh every 5 seconds
