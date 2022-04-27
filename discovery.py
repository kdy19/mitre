import subprocess
import json
import os


# 24
DISCOVERY_LOG = {
    'T1007' : {},
    'T1010' : {},
    'T1012' : {},
    'T1016' : {},
    'T1018' : {},
    'T1046' : {},
    'T1049' : {},
    'T1057' : {},
    'T1069' : {
        '001' : {},
        '002' : {}
    },
    'T1082' : {},
    'T1083' : {},
    'T1087' : {
        '001' : {},
        '002' : {}
    },
    'T1120' : {},
    'T1124' : {},
    'T1135' : {},
    'T1201' : {},
    'T1217' : {
        'Chrome' : {},
        'Edge' : {}
    },
    'T1482' : {},
    'T1518' : {
        '001' : {}
    },
    'T1614' : {
        '001' : {}
    },
    'T1615' : {}
}

class Discovery:

    def __init__(self):
        pass

    def command_run(self, cmd):
        result = subprocess.Popen(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        try:
            result = result.decode('utf-8').split('\r\n')
        except UnicodeDecodeError as e:
            result = result.decode('cp949').split('\r\n')
        
        print(f'[+] {cmd}')
        for i in result:
            print(i)

        return result
    
    def discovery_run(self):
        with open('result.json', 'rt', encoding='utf-8') as f:
            data = json.load(f)

        self.T1007()

        self.T1010()

        self.T1012()

        self.T1016()

        self.T1018()

        self.T1046()

        self.T1049()

        self.T1057()

        self.T1069_001()
        self.T1069_002()

        self.T1082()

        self.T1083()

        self.T1087_001()
        self.T1087_002()

        self.T1120()

        self.T1124()

        self.T1135()

        self.T1201()

        self.T1217()

        self.T1482()

        self.T1518_001()

        self.T1614_001()

        self.T1615()

        data['result']['discovery_log'] = DISCOVERY_LOG
        with open('result.json', 'wt', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
    def T1007(self):
        cmd_list = [
            'tasklist /svc',
            'net start'
        ]

        for idx, cmd in cmd_list:
            result = self.command_run(cmd)

            DISCOVERY_LOG['T1007'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }
    
    def T1010(self):
        cmd = 'get-process | where-object {$_.mainwindowtitle -ne ""} | Select-Object mainwindowtitle'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1010'] = {
            'command' : cmd,
            'result' : result
        }

    def T1012(self):
        cmd = 'reg query "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings"'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1012'] = {
            'command' : cmd,
            'result' : result
        }

    def T1016(self):
        cmd = 'ipconfig /all'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1016'] = {
            'command' : cmd,
            'result' : result
        }

    def T1018(self):
        cmd = 'type C:\\Windows\\System32\\Drivers\\etc\\hosts'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1018'] = {
            'command' : cmd,
            'result' : result
        }

    def T1046(self):
        cmd = 'netstat -ant'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1046'] = {
            'command' : cmd,
            'result' : result
        }

    def T1049(self):
        cmd = 'netstat -anop tcp'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1049'] = {
            'command' : cmd,
            'result' : result
        }

    def T1057(self):
        cmd = 'powershell Get-Process'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1057'] = {
            'coomand' : cmd,
            'result' : result
        }

    def T1069_001(self):
        cmd = 'net localgroup'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1069']['001'] = {
            'command' : cmd,
            'result' : result
        }
    
    def T1069_002(self):
        cmd = 'net group /domain'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1069']['002'] = {
            'command' : cmd,
            'result' : result
        }

    def T1082(self):
        cmd = 'systeminfo'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1082'] = {
            'command' : cmd,
            'result' : result
        }

    def T1083(self):
        user_name = self.command_run('whoami').split('\\')[1].replace('\r\n', '')
        cmd = f'cd C:\\Users\\{user_name} && dir'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1083'] = {
            'command' : cmd,
            'result' : result
        }

    def T1087_001(self):
        cmd = 'net user'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1087']['001'] = {
            'command' : cmd,
            'result' : result
        }

    def T1087_002(self):
        cmd_list = [
            'net user /domain',
            'net group /domain'   
        ]

        for idx, cmd in cmd_list:
            result = self.command_run(cmd)

            DISCOVERY_LOG['T1087']['002'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }

    def T1120(self):
        cmd = 'fsutil fsinfo drives'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1120'] = {
            'command' : cmd,
            'result' : result
        }
    
    def T1124(self):
        cmd = 'w32tm /tz'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1124'] = {
            'command' : cmd,
            'result' : result
        }

    def T1135(self):
        cmd = 'net share'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1135'] = {
            'command' : cmd,
            'result' : result
        }

    def T1201(self):
        cmd = 'net accounts'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1201'] = {
            'command' : cmd,
            'result' : result
        }

    def T1217(self):
        user_name = self.command_run('whoami').split('\\')[1].replace('\r\n', '')
        chrome_bookmark_path1 = f'C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks',
        chrome_bookmark_path2 = f'C:\\Users\\{user_name}\\AppData\\Local\\Google\\Chrome\\User Data',
        edge_bookmark_path = f'C:\\Users\\{user_name}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Bookmarks'

        if os.path.exists(chrome_bookmark_path1):
            with open(chrome_bookmark_path1, 'rt', encoding='utf-8') as f:
                data = json.load(f)
            DISCOVERY_LOG['T1217']['Chrome']['Default'] = data 
        else:
            for i in range(1, 5 + 1):
                if os.path.exists(chrome_bookmark_path2 + f'\\Profile {i}\\Bookmarks'):
                with open(chrome_bookmark_path2 + f'\\Profile {i}\\Bookmarks', 'rt', encoding='utf-8') as f:
                    data = json.load(f)
                DISCOVERY_LOG['T1217']['Chrome'][f'Profile {i}'] = data 

        if os.path.exists(edge_bookmark_path):
            with open(edge_bookmark_path, 'rt', encoding='utf-8') as f:
                data = json.load(f)
            DISCOVERY_LOG['T1217']['Edge'] = data
    
    def T1482(self):
        cmd_list = [
            'nltest /domain_trusts',
            'powershell Get-NetDomainTrust',
            'powershell Get-NetForestTrust'
        ]

        for idx, cmd in enumerate(cmd_list):
            result = self.command_run(cmd)
            DISCOVERY_LOG['T1482'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }

    def T1518_001(self):
        cmd = 'powershell "Get-ItemProperty HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* ' +
         '| Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table -Autosize"'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1518']['001'] = {
            'command' : cmd,
            'result' : result
        }

    def T1614_001(self):
        cmd = 'dism /online /get-intl'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1614']['001'] = {
            'command' : cmd,
            'result' : result
        }
        
    def T1615(self):
        cmd_list = [
            'powershell Get-DomainGPO',
            'powershell Get-DomainGPOLocalGroup'
        ]

        for idx, cmd in enumerate(cmd_list):
            result = self.command_run(cmd)
            DISCOVERY_LOG['T1615'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }
