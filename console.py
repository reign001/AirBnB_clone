import cmd

class HBNBCommand(cmd.Cmd):
    """
    this class defines the command line interpreter
    """
    prompt = ("hbnb")


    def do_quit(self, arg):
        """this quits or exits the programme"""
        return True

    do_EOF = do_quit
    

















if __name__ == '__main__':
HBNBCommand().cmdloop()
