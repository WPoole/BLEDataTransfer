#!/usr/bin/env python

import socket
import subprocess

def execute(command):
        popen = subprocess.Popen(command, stdout=subprocess.PIPE)
        lines_iterator = iter(popen.stdout.readline, b"")
        TCP_IP = '169.254.244.161'
        TCP_PORT = 5005
        BUFFER_SIZE = 1024


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        for line in lines_iterator:
                if "value:" not in line:
                        continue
                s.send(line.split(": ")[1])
                data = s.recv(BUFFER_SIZE)
                print data


execute(['gatttool', '-b', '00:02:5B:00:15:10', '--char-write-req', '--handle=0x0003', '--value=0100', '--listen'])