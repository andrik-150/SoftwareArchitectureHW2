class Iterator:
    def __init__(self):
        pass

    def has_next(self):
        pass

    def next(self):
        pass


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_iterator(self):
        return ConcreteIterator(self.items)


if __name__ == "__main__":
    collection = Collection()
    collection.add_item("Item 1")
    collection.add_item("Item 2")
    collection.add_item("Item 3")

    iterator = collection.create_iterator()

    while iterator.has_next():
        item = iterator.next()
        print(item)
