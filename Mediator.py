class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator


class ConcreteColleague1(Colleague):
    def send(self, message):
        self.mediator.send_message(message, self)


class ConcreteColleague2(Colleague):
    def send(self, message):
        self.mediator.send_message(message, self)


class Mediator:
    def __init__(self):
        self.colleague1 = None
        self.colleague2 = None

    def set_colleague1(self, colleague):
        self.colleague1 = colleague

    def set_colleague2(self, colleague):
        self.colleague2 = colleague

    def send_message(self, message, sender):
        if sender == self.colleague1:
            self.colleague2.receive(message)
        elif sender == self.colleague2:
            self.colleague1.receive(message)


class Client:
    def __init__(self):
        mediator = Mediator()
        colleague1 = ConcreteColleague1(mediator)
        colleague2 = ConcreteColleague2(mediator)

        mediator.set_colleague1(colleague1)
        mediator.set_colleague2(colleague2)

        colleague1.send("Привет, это коллега 1")
        colleague2.send("Привет, это коллега 2")

    @staticmethod
    def main():
        client = Client()


if __name__ == "__main__":
    Client.main()
