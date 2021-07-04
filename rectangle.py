class Rectangle:
    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh

    def getWidth(self):
        return self.width

    def getHeigh(self):
        return self.heigh
#method, which calculate area
    def getArea(self):
        return self.width * self.heigh