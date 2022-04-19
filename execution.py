from datetime import datetime
import subprocess
import json
import os


POWERSHELL_COMMAND = [
    'echo Get-ExecutionPolicy > t1059_001.ps1 && powershell .\\t1059_001.ps1'
]
EXECUTION_LOG = {
    'T1047' : {},
    'T1053' : {
        '002' : {},
        '005' : {}
    },
    'T1059' : {
        '001' : {},
        '003' : {},
        '005' : {},
        '006' : {}
    },
    'T1569' : {
        '002' : {}
    },
    'T1599' : {
        '001' : {}
    },
    'T1609' : {}
}
       
class Execution:

    def __init__(self):
        pass
    
    def execution_run():
        with open('result.json', 'rt', encoding='utf-8') as f:
            data = json.load(f)

        self.T1047()

        self.T1053_002()
        self.T1053_005()

        self.T1059_001()
        self.T1059_003()
        self.T1059_005()
        self.T1059_006()

        self.T1569_002()

        self.T1599_001()

        self.T1609()

        data['result']['execution'] = EXECUTION_LOG
        with open('result.json', 'wt', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    
    def get_powershell_policy(self):
        cmd = 'powershell Get-ExecutionPolicy'
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')[0]

        result_log = f'[+] {cmd} {result}'

        EXECUTION_LOG['Get-ExecutionPolicy'] = result_log
        if result == 'Restricted':
            return False
        else:
            return True

    def T1047(self):
        cmd_list = [
            'wmic computersystem get Name, Model, Domain, Manufacturer, Description',
            'wmic environment list',
            'wmic useraccount list',
            'wmic qfe list'
        ]

        for idx, cmd in enumerate(cmd_list):
            result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = result.decode('utf-8').split('\r\n')

            print(f'[+] {cmd}')
            for i in result:
                print(i)
            print()

            EXECUTION_LOG['T1047'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }

    def T1053_002(self):
        current_time = datetime.now()
        cmd = 'schtasks /create /tn "test" /tr C:\\Windows\\System32\\cmd.exe /sc once /sd {0}/{1}/{2} /st {3}:{4}'.format(
            current_time.year, current_time.month, current_time.day, current_time.hour, current_time.minute + 3
        )

        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)
            
        EXECUTION_LOG['T1053']['002'] = {
            'command' : cmd,
            'result' : result
        }

    def T1053_005(self):
        cmd = 'schtasks /query /fo LIST /v'

        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)

        EXECUTION_LOG['T1053']['005'] = {
            'command' : cmd,
            'result' : result
        }

    def T1059_001(self):
        flag = self.get_powershell_policy()

        if flag:
            for idx, c in enumerate(POWERSHELL_COMMAND):
                result = subprocess.Popen(c.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
                result = result.decode('utf-8').split('\r\n')

                for i in result:
                    print(i)
                
                print(f'[+] {c}')
                EXECUTION_LOG['T1059']['001'][f'{idx + 1}'] = {
                    'command' : c,
                    'result' : result
                }
        else:
            for idx, c in enumerate(POWERSHELL_COMMAND):
                print(f'[-] {c}')
                EXECUTION_LOG['T1059']['001'][f'{idx + 1}'] = {
                    'command' : c,
                }

    def T1059_003(self):
        cmd = 'wmic process call create \'calc.exe\''
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)
        
        EXECUTION_LOG['T1059']['003'] = {
            'command' : cmd,
            'result' : result
        }

    def T1059_005(self):
        VBA_COTNENT = [
            'echo RUN \'C:\\WINDOWS\\system32\\cmd.exe\' > t1059_005.vba',
            'echo Sub Run (Execute) >> t1059_005.vba',
                'echo Set wshShell = WScript.CreateObject(\'WScript.Shell\') >> t1059_005.vba',
                'echo wshShell.Run Execute >> t1059_005.vba',
                'echo Set wshShell = Nothing >> t1059_005.vba',
            'echo End Sub >> t1059_005.vba',
            '.\\t1059_005.vba'
        ]

        for c in VBA_COTNENT:
            result = subprocess.Popen(c.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = result.decode('utf-8').split('\r\n')

            for i in result:
                print(i)

        EXECUTION_LOG['T1059']['005'] = {
            'command' : VBA_CONTENT,
            'result' : result
        }

    def T1059_006(self):
        cmd = 'python -c "print(\'A\'*10)"'
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.deocde('utf-8').split('\r\n')

        if result[0] == ('A' * 10):
            print(f'[+] {cmd}')
        else:
            print(f'[-] {cmd}')

        EXECUTION_LOG['T1059']['006'] = {
            'command' : cmd,
            'result' : result
        }

    def T1569_002(self):
        cmd = 'sc create test type=own binPath="C:\Windows\System32\cmd.exe'
        
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = result.decode('utf-8').split('\r\n')

        for i in result:
            print(i)

        EXECUTION_LOG['T1569']['002'] = {
            'command' : cmd,
            'result' : result
        }

    def T1599_001(self):
        pass

    def T1609(self):
        COMMAND_LIST = ['docker ps']

        for idx, cmd in enumerate(COMMAND_LIST):
            result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = result.decode('utf-8').split('\r\n')

            for i in result:
                print(i)
    
            EXECUTION_LOG['T1609'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }