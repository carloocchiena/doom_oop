from random import choice

class Sprite:
    
    count = 0
    
    def __init__ (self, name, health, attack, alignment):
        self.name = name
        self.health = health
        self.attack = attack
        self.alignment = alignment
        
    def hit (self):
        return choice(range(self.attack))
    
    def damage(self, attack):
        self.count +=1
        self.health -= attack
        return self.health
    
    def alive (self):
        if self.health < 1:
            return False
            print (f"{self.name} is dead.")
        else:
            return True
        
    def __str__(self):
        return f"{self.name} is {self.alignment} it has {self.health} life points, been hit {self.count} times"
        
imp = Sprite("Imp", 20, 10, "evil")
revenant = Sprite("Revenant", 75, 25, "evil")
cacodemon = Sprite ("Cacodemon", 20, 15, "evil")
doomguy = Sprite ("Doomguy", 100, 25, "good" )

enemy_list = [revenant, cacodemon, imp]

def play():
    while doomguy.alive():
    
        enemy = choice(enemy_list)
        defeated_enemies = []   
              
        while enemy.alive() and doomguy.alive():
            enemy.damage(doomguy.hit())
            doomguy.damage(enemy.hit())
            print (doomguy)
            print (enemy)
        else:
            enemy = choice(enemy_list)
 
        for i in enemy_list:
            if i.health <1:
                defeated_enemies.append(i.name)
    
    else:
        print (f"{doomguy.name}'s' dead.")
        print (f"Doomguy defeated: {defeated_enemies}")
        print ("Game Over")

play()
