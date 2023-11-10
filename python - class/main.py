class Animal:
  name = "" # properties / attribute
  color = ""

  

  def makeSound(self, sound):  # method
    print(f"{self.name} is {sound}")

  def eat(self, food):
    print(f"{self.name} is eating {food}")

  def sleep(self):
    print(f"{self.name} is sleeping")

cat = Animal()
cat.name = "Bravo"
cat.makeSound("Meowing")