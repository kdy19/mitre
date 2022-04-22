import subprocess


class Persistence:

    def __init__(self):
        pass

    def persistence_run(self):
        self.T1136_001()


    def T1136_001(self):
        cmd_list = [
            'net user t1136_001 P@assw0rd! /add',
            'net user',
            'net user t1136_001 /active:no'
        ]

        for cmd in cmd_list:
            result = subprocess.Poepn(cmd.split(' '), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
            result = result.decode('utf-8').split('\r\n')

            print(f'[+] {cmd}')
            for i in result:
                print(i)
    