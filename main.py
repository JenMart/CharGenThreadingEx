import threading
import time
import random

#   Taken from previous project

firstHalf = "Ger Symart Hugh Ger Byssh Riff Vin Heg Gile Gau Ewl Gyl" \
                  "Rar Helm Thu Coel Erf Cane folke Knett Leneth Dene Hav Tun Thun".split() #24
seconHalf = "y ey te nah ney ley walt wort man der dar dor da neth ke fin son kin".split() #18
nickName1 = "Tongue Preserver Mouth Phantom Wonder Guardian Watcher Fist " \
                    "Slayer Hammer Sword Arrow".split() #12
nickName2 = "Big Small Flamming Last First Great Final Burning Smug".split()
job = ["Warrior", "Thief","Barbarian","Warrior Priest","Knight","Paladin"]
#   Takes random words and syllables to generate a name, nickname and class

class Character: #where generation takes place.
    def __init__(self, num):
        self.number = num
        self.nameOne = random.choice(firstHalf)
        self.nameTwo = random.choice(seconHalf)
        self.nickName = random.choice(nickName2) + " " + random.choice(nickName1)
        self.className = random.choice(job)

    def name(self):
        chara = ' '.join(['The', self.nickName + '.','You are a', self.className])
        print chara

    def traits(self):
        trts = ' '.join(['\nYou are', self.nameOne + self.nameTwo])
        print trts


#   generate_character
#   Makes a new charatcer and makes it wait for a short period of time. Characters name is generated
#   in multiply pieces simultaneously to display how multiple threads can work at the same time.
def generate_character(i):
    ch = Character(i)
    time.sleep(i)
    ch.traits()
    time.sleep(1)
    ch.name()



#   main method.
#   Generates several threads simultaneously.
def main():
    for i in range(5):
        t = threading.Thread(target=generate_character, args=(i,))
        t.start()


main()
