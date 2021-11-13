from abc import ABC, abstractmethod

class AbstractMethod(ABC):

    @abstractmethod
        # @ is used to write a decorator in python  
    def abstract_method(self):
        pass