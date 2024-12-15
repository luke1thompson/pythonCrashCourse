class Character:
    # stores the stats and attributes of a character in a video game
    
    def __init__(self, name, job):
        self.name = name.title()
        self.job = job.lower()
        self.statsonlevel = statarray(job)
        self.stats = {'str':5, 'dex':5, 'mag':5, 'wil':5}
        self.lvl = 1
        self.equipment = {}
        
    def status(self):
        message = (
            f"{self.name} is a level {self.lvl} {self.job} and has :\n"
            f"{self.stats['str']} strength\n{self.stats['dex']} dexterity\n"
            f"{self.stats['mag']} magic\n{self.stats['wil']} willpower"
            )
        print(message)
        
    def equip(self, id, slot):
        self.equipment[slot] = id
    
    def lvlup(self, levels=1):
        self.stats['str'] += self.statsonlevel[0] * levels
        self.stats['dex'] += self.statsonlevel[1] * levels
        self.stats['mag'] += self.statsonlevel[2] * levels
        self.stats['wil'] += self.statsonlevel[3] * levels
        self.lvl += 1 * levels
        
    def inventory(self):
        for slot, item in self.equipment.items():
            print(f"{self.name} is wearing a {item} on their {slot}.")


class NPC(Character):
    # A character outside of the players control
    
    def __init__(self, name, job, type='dumb'):
        super().__init__(name, job)
        # initialize attributes of the parent class
        self.ai = Ai(type)
        
    def inspect(self):
        print(f"{self.name} is {self.ai.describeAi()}")
        for slot, item in self.equipment.items():
            print(f"They are wearing a {item} on their {slot}.")
            
    def lvlup(self):
        self.job += '+'


class Ai:
    def __init__(self, type):
        self.type = type
        
    def describeAi(self):
        return self.type
            
def statarray(job):
    # The four items in the list correspond to:
    # ['str', 'dex', 'mag', 'wil']
    match job:
        case 'soldier':
            return [4,3,0,2]
        case 'thief':
            return [2,4,2,1]
        case 'scholar':
            return [1,2,4,2]
        case 'cleric':
            return [1,1,3,4]
        case _:
            return [3,2,2,2]

player1 = Character('luke', 'cleric')
rando1 = NPC('jimmy', 'peasant')
player1.equip('steel cap', 'head')
rando1.equip('assless chaps', 'crotch')
player1.inventory()
rando1.lvlup()
rando1.inspect()