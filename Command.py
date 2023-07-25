class Receiver:
    def action(self):
        print("Receiver выполняет действие")


class Command:
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action()


class Invoker:
    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()


if __name__ == "__main__":
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()

    invoker.set_command(command)
    invoker.execute_command()
