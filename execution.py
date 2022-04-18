from datetime import datetime
import subprocess
import os


POWERSHELL_COMMAND = [
    'echo Get-ExecutionPolicy > t1059_001.ps1 && powershell .\\t1059_001.ps1'
]

class CommandAndScripting:

    def __init__(self):
        pass

    def get_powershell_policy(self):
        cmd = 'powershell Get-ExecutionPolicy'
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')[0]

        print(f'[+] {cmd} {result}')

        if result == 'Restricted':
            return False
        else:
            return True

    def T1059_001(self):
        flag = self.get_powershell_policy()

        if flag:
            for c in POWERSHELL_COMMAND:
                result = subprocess.Popen(c.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
                result = result.decode('utf-8').split('\r\n')

                for i in result:
                    print(i)
                
                print(f'[+] {c}')
        else:
            for c in POWERSHELL_COMMAND:
                print(f'[-] {c}')

    def T1059_003(self):
        cmd = 'wmic process call create \'calc.exe\''
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            prinnt(i)

    def T1059_005(self):
        VBA_COTNENT = [
            'echo RUN \'C:\\WINDOWS\\system32\\cmd.exe\' > t1059_003.vba',
            'echo Sub Run (Execute) >> t1059_003.vba',
                'echo Set wshShell = WScript.CreateObject(\'WScript.Shell\') >> t1059_003.vba',
                'echo wshShell.Run Execute >> t1059_003.vba',
                'echo Set wshShell = Nothing >> t1059_003.vba',
            'echo End Sub >> t1059_003.vba',
            '.\\t1059_003.vba'
        ]

        for c in VBA_COTNENT:
            result = subprocess.Popen(c.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = result.decode('utf-8').split('\r\n')

            for i in result:
                print(i)

    def T1059_006(self):
        cmd = 'python -c "print(\'A\'*10)"'
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.deocde('utf-8').split('\r\n')[0]

        if result == ('A' * 10):
            print(f'[+] {cmd}')
        else:
            print(f'[-] {cmd}')

       
class Execution:

    def __init__(self):
        pass
    
    def T1047(self):
        cmd_list = [
            'wmic computersystem get Name, Model, Domain, Manufacturer, Description',
            'wmic environment list',
            'wmic useraccount list',
            'wmic qfe list'
        ]

        for cmd in cmd_list:
            result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = result.decode('utf-8').split('\r\n')

            print(f'[+] {cmd}')
            for i in result:
                print(i)
            print()

    def T1053_002(self):
        current_time = datetime.now()
        cmd = 'schtasks /create /tn "test" /tr C:\\Windows\\System32\\cmd.exe /sc once /sd {0}/{1}/{2} /st {3}:{4}'.format(
            current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute + 3
        )

        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)

    def T1053_005(self):
        cmd = 'schtasks /query /fo LIST /v'

        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)

    def T1569_002(self):
        cmd = 'sc create test type=own binPath="C:\Windows\System32\cmd.exe'
        
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)

    def T1599_001(self):
        pass

    def T1609(self):
        COMMAND_LIST = ['docker ps']

        print(f'[+] {c}')
        for c in COMMAND_LIST:
            p = subprocess.Popen(c.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = p.decode('utf-8').split('\r\n')

            for i in result:
                print(i)
    