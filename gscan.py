import socket
import termcolor
import colorama
import sys
import time


colorama.init()


host = input("Target->: ")
maxPort = int(input("How many ports do you want to scan->: "))
termcolor.cprint(f"Scanning up to port: {maxPort}.", 'blue')
termcolor.cprint("Port scan started on: " + str(time.ctime()))
maxPort = (maxPort + 1)


def scanPorts(ports):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.2)
    if s.connect_ex((host, ports)):
        termcolor.cprint(f"Port: {ports} is closed.", 'red')
        s.close()
    else:
        termcolor.cprint(f"Port: {ports} is open", 'green')
        s.close()


for ports in range(1, maxPort):
    scanPorts(ports=ports)


termcolor.cprint("Port scan finished on: " + str(time.ctime()))


sys.exit(0)