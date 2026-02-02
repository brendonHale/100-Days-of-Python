class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("Swimming.")

    def breathe(self):
        super().breathe()
        print("Underwater")

nemo = Fish()
nemo.swim()
nemo.breathe()