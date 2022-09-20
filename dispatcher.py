import re
import sys
import discord

class dispatcher:
    def __init__(self):
        self.builtins = {}
        self.cmds = {}
        self.default = lambda x: x

    def register_builtin(self,match,handler):
        m = re.compile(match)
        self.builtins[m] = (handler,None,None)

    def register_cmd(self,match,handler,roles=None,channels=None):
        m = re.compile(match)
        self.cmds[m] = (handler,roles,channels)

    def register_default(self,handler):
        self.default = handler

    def check_cmd_permission(self,message,handler):
        _,roles,channels = handler
        if roles:
            pass
        if channels:
            if message.channel.type != discord.ChannelType.text:
                return False
            for channel in channels:
                if re.search(channel,message.channel.name):
                    return True
            return False
        return True

    async def dispatch_cmd(self,message):
        for cmd,handler in self.builtins.items():
            if cmd.match(message.content):
                await handler[0](message)
                return
        for cmd,handler in self.cmds.items():
            if cmd.match(message.content):
                if self.check_cmd_permission(message,handler):
                    await handler[0](message)
                    return
        self.default(message)
