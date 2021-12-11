import random
class makeCH():

    def __init__(self):
        self.hp = random.randrange(1000, 1500)
        self.mp = random.randrange(1700, 2000)
    def hit(self):
        return self.hp - 20
    def heal(self):
        self.hp=self.hp + 120
        self.mp=self.mp - 60





player = makeCH()
print("player character hp : {}, mp : {}".format(player.hp, player.mp))

ai = makeCH()
print("ai character hp : {}, mp : {}".format(ai.hp, ai.mp))

# player 스킬 쓰기
# a = int(input("enter your skiil : "))
# if a == 5:
#     a = ai.hp = ai.hit()
# elif a == 6:
#     a == player.heal()

# ai 스킬 쓰기
# b = int(random.randrange(0, 1))
# if b == 0:
#     b = player.hit()
# elif b == 1:
#     b = ai.heal()
# elif ai == 2
# elif ai == 3
# elif ai == 4

while True:
    if player.hp <= 0:
        print("after player hp : {}, mp : {}".format(player.hp, player.mp))
        print("after ai hp : {}, mp : {}".format(ai.hp, ai.mp))
        print('패배')
        break
    elif ai.hp <= 0:
        print("after player hp : {}, mp : {}".format(player.hp, player.mp))
        print("after ai hp : {}, mp : {}".format(ai.hp, ai.mp))
        print('승리')
        break
    elif player.hp > 0 and ai.hp > 0:
        # player 스킬 쓰기
        a = int(input("enter your skiil : "))
        if a == 5:
            a = ai.hp = ai.hit()
        elif a == 6:
            a == player.heal()
        print("1.after player hp : {}, mp : {}".format(player.hp, player.mp))
        print("1.after ai hp : {}, mp : {}".format(ai.hp, ai.mp))
        # ai 스킬 쓰기
        b = int(random.randrange(0, 2))
        if b == 0:
            b = player.hit()
        elif b == 1:
            b = ai.heal()
        print("2.after player hp : {}, mp : {}".format(player.hp, player.mp))
        print("2.after ai hp : {}, mp : {}".format(ai.hp, ai.mp))

# ai hit으로 맞는 것
# ai.hp = ai.hit()

# ai가 본인 heal 하는 것
# ai.heal()


#  player 스킬 쓰기
# a = int(input("enter your skiil : "))
# if a == 5:
#     a = ai.hp = ai.hit()
#     print("after ai hp : {}, mp : {}".format(ai.hp, ai.mp))
# elif a == 6:
#     a == player.heal()

# ai 스킬 쓰기
# b = int(random.randrange(0, 1))
# if b == 0:
#     b = player.hit()
# elif b == 1:
#     b = ai.heal()
# elif ai == 2
# elif ai == 3
# elif ai == 4
