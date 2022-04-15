import subprocess


class CommandAndScripting:

    def T1059_001():
        pass

       
class Execution:

    def __init__():
        pass

    def T1609():
        
        COMMAND_LIST = ['docker ps']

        p = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
        result = p.decode('utf-8').split('\r\n')

        for i in result:
            print(i)
