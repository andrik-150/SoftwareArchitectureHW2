class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def do_some_work(self):
        self._strategy.execute()


class Strategy:
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Выполнение стратегии A.")


class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Выполнение стратегии B.")


if __name__ == "__main__":
    # Начальная стратегия - A
    initial_strategy = ConcreteStrategyA()
    context = Context(initial_strategy)

    # Выполнение работы с начальной стратегией
    context.do_some_work()

    # Изменение стратегии на B и выполнение работы с новой стратегией
    new_strategy = ConcreteStrategyB()
    context.set_strategy(new_strategy)
    context.do_some_work()
