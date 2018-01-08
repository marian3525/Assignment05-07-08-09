from ui import readCommand
def run():
    cmd = readCommand()
    command = cmd[0]
    params = cmd[1]
    print(command)
    print(params)

run()