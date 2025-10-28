from abc import ABC, abstractmethod


class BaseCalc(ABC):

    @abstractmethod
    def calc(self):
        pass
