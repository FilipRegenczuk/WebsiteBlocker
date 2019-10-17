# WebsiteBlocker
Application blocking opening selected websites during working hours. Written in Python.

# Usage
At the beginning you need to change some lines in app.pyw script:
1. hosts_path - your path to the hosts:
  - for Windows: C:\Windows\System32\drivers\etc\hosts
  - for Linux or Mac: /etc/hosts
2. blocked_websited - websites you want to block
3. in while loop in first if statement you can change hours while the application is working

# Installation
A) for Windows:
  1. Open Task Scheduler -> Create Basic Task -> In generals: Enter name -> In triggers: add 'New...' and set 'Begin the task' to 'At startup'
  -> In actions: add 'New...' and set 'Action' to 'Start a program', in 'Program/script' find app.pyw and add it -> In conditions: in Power
    section unhook 'Start the task only if the computer is on AC power'
  2. In Task Scheduler in upper section find Website Blocker you can turn on and turn off Website Blocker
  
B) for Linux and Mac:
  1. Install crontab
  2. Open terminal in folder where app.pyw is
  3. Enter: 'sudo crontab -e'
  4. At the end enter: '@reboot python3 /destination_of_the_website_blocker_/app.pyw'
  5. Click Ctrl+X -> y -> Enter
