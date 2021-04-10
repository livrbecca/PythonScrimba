# Inheritance - you have a class, and another class can inherit its attributes
# confirm that these dont need initialising because tehres no attributes apart from self?
class Person:
    def move(self):
        print("Moves 4 paces")

    def rest(self):
        print("Gains 4 health points")


class Doctor(Person):  # doctor will inherit rest and move from person
    def heal(self):
        print("Heals 10 health points")


class Fighter(Person):
    def fight(self):
        print("Damage: -10 health points")

    def move(self):
        print("Moves 6 paces")


class Wizard(Doctor):
    def cast_spell(self):
        print("Tunrs invisible")

    def heal(self):
        print("Heals 15 health points")


ch1 = Person()
ch1.move()

ch2 = Doctor()
ch2.rest()

ch3 = Fighter()
# ch3.heal() doesnt work because not inherited from Doctor
ch3.fight()
ch3.move()  # overwritten the original 'move' method

ch4 = Wizard()
ch4.heal() # overwritten the original 'heal' method from Doctor
ch4.cast_spell()
ch4.move() # Wizard can move, inherited from Doctor who inherited it from Person - multiple inheritance
