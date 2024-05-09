import os
import time
import random
import sys

os.system("clear")
os.system("python3 src/logo.py")

print("1. DoS an Ip Address")
print("2. DoS a Url ")
print("3. Exit")
op=int(input("Options: "))
if(op==1):
 os.system("python3 src/dos.py")
elif(op==2):
 os.system("python3 src/Url.py")
elif(op==3):
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Reloading Tools!") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd SYTCS DoS")
 os.system("python3 main.py")


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
