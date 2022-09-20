import re
class dispatcher:
    def __init__(self):
        self.builtins = {}
        self.cmds = {}
        self.default = lambda x: x

    def register_builtin(self,match,cmd):
        m = re.compile(match)
        self.builtins[m] = cmd

    def register_cmd(self,match,cmd):
        m = re.compile(match)
        self.builtins[m] = cmd

    def register_default(self,cmd):
        self.default = cmd

    async def dispatch_cmd(self,message):
        for cmd,handler in self.builtins.items():
            if cmd.match(message.content):
                await handler(message)
                return
        for cmd,handler in self.cmds.items():
            if cmd.match(message.content):
                await handler(message)
                return
        self.default(message)
