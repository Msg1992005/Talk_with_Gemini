# For first time remove the indents to install require packages
# system("pip install google-generativeai")
commands = {
    "ls" : "what Commands are available",
    "chat": "normal chat with gemini",
    "login": "For registering your Api key and name on your local server",
    "prochat":"chat with gemini vision with image name",
    "exit" : "to exit the terminal",
    "clear" : "to clear your terminal",
}
class myterminal:
    def __init__(self,cmd):
        self.command = cmd
        self.commands = commands
        
    def ls_command(self):
        for command in self.commands:
            print(f"{command} : {commands[command]}")
            
    def prochat_command(self):
        pass
    def clear_command(self):
        from os import system
        system("cls")
        del os
    def login_command(self):
        pass
    def exit_command(self):
        exit()
    def mycmd(self):
        match self.command:
            case "ls":
                self.ls_command()
            case "chat":
                from mygemini import chat_command
                chat_command()
            case "exit":
                self.exit_command()
            case "clear":
                self.clear_command()
            case _:
                if (self.command in commands):
                    print("coming soon")
                else:
                    print("Wrong CMD")

        
if (__name__=="__main__"):
    terminalstate = True
    while terminalstate:
        terminal_inputs = input("Terminal # ")
        terminal = myterminal(terminal_inputs)
        terminal.mycmd()

