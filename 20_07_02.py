class Warrior:
    def __init__(self, health = 50, attack = 5):
        self.health = health
        self.attack = attack
    @property
    def is_alive(self):
        return self.health > 0

    def loose(self, damage):
        self.health -= damage

    def hit(self, enemy):
        enemy.loose(self.attack)

class Defender(Warrior):
    def __init__(self, health=60, attack=3,defense=2):
        super().__init__(health,attack)
        self.defense = defense

    def loose(self, damage):
        if damage > self.defense:
            self.health -= damage - self.defense

class Knight(Warrior):
    def __init__(self, health=50, attack=7):
        super().__init__(health, attack)
class Army:
    def __init__(self):
        self.units = []
    def add_units(self, unit_type, unit_count):
        self.units += [unit_type() for i in range(unit_count)]

class Battle:
    def fight(self, army1, army2):
        while army1.units and army2.units:
            fight_res = fight(army1.units[0], army2.units[0])
            if fight_res:
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return bool(army1.units)
def fight(unit1, unit2):
    while unit1.is_alive and unit2.is_alive:
        unit1.hit(unit2)
        if unit2.is_alive:
            unit2.hit(unit1)
    return unit1.is_alive

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)
    army_4 = Army()
    army_4.add_units(Warrior, 2)
    battle = Battle()
    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")


