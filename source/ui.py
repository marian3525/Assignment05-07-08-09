def readCommand():
    params = ""
    cmd = input(">>")

    if cmd.find(" ") == -1:
        command = cmd
    else:
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(""):]
        params.split(" ")
        for x in params:
            x.strip(" ")
    return (command, params[1:])