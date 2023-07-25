class Handler:
    def set_next(self, handler):
        pass

    def handle(self, request):
        pass


class ConcreteHandler1(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        if request == "A":
            print("ConcreteHandler1 обрабатывает запрос A")
        elif self.next_handler:
            self.next_handler.handle(request)


class ConcreteHandler2(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        if request == "B":
            print("ConcreteHandler2 обрабатывает запрос B")
        elif self.next_handler:
            self.next_handler.handle(request)


class ConcreteHandler3(Handler):
    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, request):
        if request == "C":
            print("ConcreteHandler3 обрабатывает запрос C")
        elif self.next_handler:
            self.next_handler.handle(request)


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()

    handler1.set_next(handler2)
    handler2.set_next(handler3)

    handler1.handle("A")
    handler1.handle("B")
    handler1.handle("C")
