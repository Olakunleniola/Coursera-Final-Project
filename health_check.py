#! /usr/bin/env python3
import psutil
import socket
import health_emails

def check_cpu_usage():
    return psutil.cpu_percent(1) > 80
def check_disk_space():
    d = psutil.disk_usage('/')
    return d.percent < 20
def check_memory():
    d = psutil.disk_usage('/')
    return d.free/2**30 < 0.5
def check_hostname():
    if socket.gethostbyname('localhost') == "127.0.0.1":
        return False
    return True

def main(): 
    checks = [(check_cpu_usage,'Error - CPU usage is over 80%'), (check_disk_space,'Error - Available disk space is less than 20%'),
             (check_memory,'Error - Available memory is less than 500MB'),(check_hostname,'Error - localhost cannot be resolved to 127.0.0.1')]
    body = 'Please check your system and resolve the issue as soon as possible.'
    for check,msg in checks:
        if check():
            sender = 'akandeola48@gmail.com'
            recipient = 'arrowofGod@ymail.com'
            message = emails.generate_no_attachment(sender,recipient,msg,body)
            health_emails.send(message,sender)
            print(msg+ ' sent via mail')
        else:
            print("Everything is OK!!!!")
        
if __name__ == '__main__':
    main()
