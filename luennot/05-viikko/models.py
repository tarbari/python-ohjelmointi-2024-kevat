class Fruit:
    def __init__(self, id, name, count) -> None:
        self.id = id
        self.name = name
        self.count = count

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, count={self.count})"


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass
