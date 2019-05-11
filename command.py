import subprocess

class Command:
    """a class for handling system commands"""
    def __init__(self, command):
        self.command = command
        self.is_executed = False
        self.is_done = False

    def execute(self):
        self.child = subprocess.Popen(self.command, stdout=subprocess.PIPE, shell=True)
        self.is_executed = True

    def done(self):
        if self.is_executed:
            if self.child.poll() is not None:
                self.is_done = True
                return True
            else:
                return False
        else:
            raise ValueError('completion checked before execution')

    def result(self):
        if self.is_done:
            return self.child.communicate()[0].decode()
        else:
            raise ValueError('result called before the command was done')
