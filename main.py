from initial_access import InitialAccess
from execution import Execution

from winreg import *
import json


def init():
    result_json = {'result' : {
        'initial_access_log' : {},
        'execution_log' : {},
        'persistence_log' : {}
    }}
    with open('result.json', 'wt', encoding='utf-8') as f:
        json.dump(result_json, f, indent=4)

    PATH = 'SYSTEM\\CurrentControlSet\\Control\\Nls\\CodePage'
    reg_handle = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
    try:
        key = OpenKey(reg_handle, PATH, 0, KEY_WRITE)
        try:
            SetValueEx(key, 'OEMCP', 0, REG_DWORD, '65001')
            CloseKey(key)
            CloseKey(reg_handle)
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


def initial_access_run():
    with open('setting.json', 'rt') as f:
        data = json.load(f)

    target = data['info']['server_address']
    ssh = data['info']['services']['ssh']
    telnet = data['info']['services']['telnet']
    ia = InitialAccess(target, ssh, telnet)
    ia.initial_access_run()


def execution_run():
    exe = Execution()
    exe.execution_run()


def main():
    init()
    initial_access_run()
    execution_run() 


if __name__ == '__main__':
    main()
