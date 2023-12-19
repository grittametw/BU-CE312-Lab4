class Box():
    Radius = 5
    Height = 10
    def calculate(self):
        self.Measure = 3.14 * (self.Radius * self.Radius) * self.Height
        return self.Measure

FirstBox = Box()
SecondBox = Box()
SecondBox.Radius = 7
SecondBox.Height = 13

print ("First box measure = ", FirstBox.calculate())
print ("Second box measure = ", SecondBox.calculate())