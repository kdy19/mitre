from initial_access import ValidAccounts
from execution import CommandAndScripting
from execution import Execution

import json


def initial_access_run():
    with open('setting.json', 'rt') as f:
        data = json.load(f)

    target = data['info']['server_address']
    ssh = data['info']['services']['ssh']
    telnet = data['info']['services']['telnet']
    va = ValidAccounts(target, ssh, telnet)
    va.T1078_003()


def execution_run():
    cas = CommandAndScripting()
    cas.T1059_001()
    cas.T1059_003()
    cas.T1059_005()
    cas.T1059_006()

    exe = Execution()

    exe.T1047()

    exe.T1053_002()
    exe.T1053_005()

    exe.T1569_002()

    exe.T1599_001()
    
    exe.T1609()


def main():
    initial_access_run()
    execution_run() 


if __name__ == '__main__':
    main()
