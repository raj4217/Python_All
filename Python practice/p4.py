from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def __init__(self,width,length):
        self.width = width
        self.length = length

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass


class rectangle(shape):

    def __init__(self,width,length):
        super().__init__(width,length)
        if self.width == self.length:
            print('its a Square')
        else: print('its a rectangle')

    def area(self):
        return self.width*self.length

    def perimeter(self):
        return 2*(self.width+self.length)

# r =rectangle(20,40)
# print(r.area())

s = rectangle(40,40)
print(s.perimeter())

