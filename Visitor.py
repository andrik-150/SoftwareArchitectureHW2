class Visitor:
    def visit_element_a(self, element_a):
        pass

    def visit_element_b(self, element_b):
        pass


class ConcreteVisitor1(Visitor):
    def visit_element_a(self, element_a):
        print("ConcreteVisitor1 посещает ElementA")

    def visit_element_b(self, element_b):
        print("ConcreteVisitor1 посещает ElementB")


class ConcreteVisitor2(Visitor):
    def visit_element_a(self, element_a):
        print("ConcreteVisitor2 посещает ElementA")

    def visit_element_b(self, element_b):
        print("ConcreteVisitor2 посещает ElementB")


class Element:
    def accept(self, visitor):
        pass


class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)


class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)


if __name__ == "__main__":
    element_a = ElementA()
    element_b = ElementB()

    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    element_a.accept(visitor1)
    element_a.accept(visitor2)

    element_b.accept(visitor1)
    element_b.accept(visitor2)
