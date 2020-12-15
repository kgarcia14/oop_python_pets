class Pet:
     def __init__(self, name, fullness=50, happiness=50, hunger=10, mopiness=10):
          self.name = name
          self.fullness = fullness
          self.happiness = happiness
          self.hunger = hunger
          self.mopiness = mopiness

     def feed_pet(self):
          self.fullness += 30
     
     def play_with_pet(self):
          self.happiness += 30

     def get_hungry_and_mopey(self, hunger, mopiness):
          self.fullness -= self.hunger
          self.happiness -= self.mopiness/2

class CuddlyPet(Pet):
     def cuddle(self, other_pet):
          other_pet.play_with_pet()


lola = CuddlyPet("Lola", 50, 20, 20, 1) 
rio = Pet("Rio", 50, 10, 30, 10)
print(rio.happiness)

lola.cuddle(rio)
print(rio.happiness)


