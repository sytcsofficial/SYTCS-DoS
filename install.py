import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 main.py')
    run('mkdir /usr/share/sytcsdos')
    run('cp main.py /usr/share/sytcsdos/main.py')
    run('cp -r src /usr/share/sytcsdos/src')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/sytcsdos/main.py"$@"')
    with open('/usr/bin/sytcsdos','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/sytcsdos & chmod +x /usr/share/sytcsdos/main.py')
    print('''\n\ncongratulation SYTCS DoS is installed successfully \nfrom now just type \x1b[6;30;42msytcsdos\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/sytcsdos ')
    run('rm /usr/bin/sytcsdos ')
    print('[!] now SYTCS DoS has been removed successfully')





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
