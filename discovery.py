import subprocess
import json
import os


DISCOVERY_LOG = {
    'T1087' : {
        '001' : {},
        '002' : {}
    },
    'T1010' : {}
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

        self.T1087_001()
        self.T1087_002()

        self.T1010()

        data['result']['discovery_log'] = DISCOVERY_LOG
        with open('result.json', 'wt', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    
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
    
    def T1010(self):
        cmd = 'get-process | where-object {$_.mainwindowtitle -ne ""} | Select-Object mainwindowtitle'
        result = self.command_run(cmd)

        DISCOVERY_LOG['T1010'] = {
            'command' : cmd,
            'result' : result
        }

    def T1217(self):
        pass

