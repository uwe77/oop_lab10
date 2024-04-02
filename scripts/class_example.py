class animal():
    def __init__(self, name='animal', age=0):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} and {self.age} years old."
    def speak(self):
        print("I'm", self)

class dog(animal):
    def __init__(self, name='dog', age=0):
        super().__init__(name, age)
    def speak(self):
        print("WOFF!! I'm", self)

class mazigou(dog, animal):
    def __init__(self, name='you', age=18):
        super().__init__(name, age)
    def speak(self):
        animal.speak(self)
    def talktogirlfriend(self):
        super().speak()

if __name__ == "__main__":
    a = animal()
    a.speak()
    d = dog()
    d.speak()
    m = mazigou()
    m.speak()
    m.talktogirlfriend()