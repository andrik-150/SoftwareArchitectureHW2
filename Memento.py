class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        print(f"Установка состояния: {state}")
        self._state = state

    def create_memento(self):
        print("Создание снимка состояния")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Восстановление состояния: {self._state}")


if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("Состояние 1")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("Состояние 2")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("Состояние 3")
    # Восстановление до второго состояния
    originator.restore_from_memento(caretaker.get_memento(1))
