class CommandParser:
    def __init__(self, separatorChar):
        self.__separatorChar = separatorChar
        self.__command = ""
        self.__params = []

    def readCommand(self):
        """
        Read a command from the console and return the command string and the parameter list
        """
        cmds = input(">>>")
        if cmds.find(self.__separatorChar) == -1:
            command = cmds
            params = []
        else:
            command = cmds[0:cmds.find(self.__separatorChar)]
            params = cmds[cmds.find(self.__separatorChar):]
            params = params.split(self.__separatorChar)

            for param in params:
                param.strip(self.__separatorChar)

        self.__command = command
        self.__params = params[1:]

    def getCommand(self):
        return self.__command

    def getParams(self):
        return self.__params
