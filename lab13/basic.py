from abc import ABC, abstractmethod


class Eat(ABC):
    @abstractmethod
    def e(self):
        pass

    @abstractmethod
    def c(self):
        pass
