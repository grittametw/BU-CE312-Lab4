class Pyramid():
    def __init__(self,InL,InW,InH):
        self.Length = Length_Class(InL)
        self.Width = Width_Class(InW)
        self.Height = Height_Class(InH)
    def Volume(self):
        Volume = (self.Length.Value * self.Width.Value * self.Height.Value) / 3
        return Volume

class Width_Class():
    def __init__(self,InputW):
        self.Value = InputW

class Length_Class():
    def __init__(self,InputL):
        self.Value = InputL

class Height_Class():
    def __init__(self,InputH):
        self.Value = InputH

Pyramid = Pyramid(10,7,17)

print(Pyramid.Length)
print(Pyramid.Width)
print(Pyramid.Height)
print("Pyramid measure = ", Pyramid.Volume())