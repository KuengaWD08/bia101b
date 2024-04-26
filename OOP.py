#Properties of Objects

class Dog:
    def __init__(self,breed,age,color,name):
        self.breed= breed
        self.color= color
        self.age= age
        self.name= name
    def bark(self):
        print("Woof! Woof!")
    def sleep(self):
        print("Zzzz...")
    def eat(self):
        print("Nom nom nom!")
    def run(self,speed):
        print("Okay i will run in",str(speed),"km/hr")

    def say_age(self):
        words_today="I am" +" "+ str(self.age)+" "+ "Years Old"
        print(words_today)
    def introduce(self):
        tell = "Hello la" + " i am " + (self.breed) + " Dog"
        say = "I am" + " "+ (self.color) +" in  color"
        print(tell)
        print(say)

    #init=initialization
    #put self init whenever under a class 
dog = Dog('Apsoo',20,'white','Dawa')
chanchi= Dog("Stray",12,'Black','Drolo')

chanchi.introduce()
chanchi.say_age()
print(chanchi.name)
dog.run(600)