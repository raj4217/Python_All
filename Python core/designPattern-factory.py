class shapeInterface():
    def draw(self): pass


class circle(shapeInterface):
    def draw(self): print('Circle.draw')


class square(shapeInterface):
    def draw(self): print('Square.draw')


class shapeFactory:
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return circle()
        if type == 'square':
            return square()
        assert 0, "Couldn't find shape" + type


f = shapeFactory
s = f.getShape('triangle')
print(s)
s.draw()
