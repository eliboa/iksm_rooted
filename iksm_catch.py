#!/usr/bin/env python
#
import paramiko, re

# Android rooted device SSH settings
host = '192.168.1.99';
username = 'root'
password = 'your_password'
cookie_path = '/data/data/com.nintendo.znca/app_webview/Cookies'

def main():

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command('cat ' + cookie_path + ' | grep iksm')
        stdout=stdout.readlines()
        try:
            iksm_session = re.findall(r'iksm_session([0-9A-Fa-f]*)/', stdout[0])[0]
            print 'Here is your iksm_session :'
            print iksm_session
        except:
            print 'Cannot find iksm_session in ' + cookie_path + '. You should try to sign in nintendo switch android app then restart this script'

        ssh.close()
    except:
        print 'Cannnot connect to ' + host

    input()

if __name__ == '__main__':
    main()
