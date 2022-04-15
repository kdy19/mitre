from initial_access import ValidAccounts

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


def main():
    # initial_access_run()
    Execution.T1609()


if __name__ == '__main__':
    main()
