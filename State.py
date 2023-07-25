# Контекст (Context)
class Context:
    def __init__(self, state):
        self._state = state

    def request(self):
        self._state.handle()

    def set_state(self, state):
        self._state = state


# Интерфейс Состояния (State)
class State:
    def handle(self):
        pass


# Конкретные состояния (Concrete States)
class ConcreteStateA(State):
    def handle(self):
        print("Обработка запроса в состоянии A.")
        print("Переключение состояния на B.")
        # Переключение состояния на B
        context.set_state(ConcreteStateB())


class ConcreteStateB(State):
    def handle(self):
        print("Обработка запроса в состоянии B.")
        print("Переключение состояния на A.")
        # Переключение состояния на A
        context.set_state(ConcreteStateA())


if __name__ == "__main__":
    # Начальное состояние - A
    initial_state = ConcreteStateA()
    context = Context(initial_state)

    # Последовательные запросы
    context.request()
    context.request()
    context.request()

