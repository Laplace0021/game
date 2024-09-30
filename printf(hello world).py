Hp_player= 1000
#notification HP
def playerHP():

    if(Hp_player <= 20 and Hp_player < 100):
        print("use healing potion")
    elif(Hp_player == 100):
        print("you are healthy")
    elif(Hp_player > 100):
        print("you are\t overheal")
    else:
        print("you good")

playerHP()