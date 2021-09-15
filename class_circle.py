class Circle :
    r = None
    def __init__(self, radius=20) :
        print("Creates a Circle object")
        self.r = radius

    def setR(self, radius) :
        self.r = radius

    def calcArea(self) :
        area = self.r * self.r * 3.14
        print("Area of circle ", area)

    def calcRound(self) :
        line = 2*self.r * 3.14
        print("Line of circle", line)



c1 = Circle()
print(c1.r)

c1.setR(10)
print(c1.r)

c1.calcArea()
c1.calcRound()
