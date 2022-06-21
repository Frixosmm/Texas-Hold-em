#This function will receive as input, ( player class, decision profile, game state)

#Will alter Player.move according to decision
#Can start smaller. Input is p.value,p.money,p.bid,pot,


def Decide_move(player):
    move="fold"
    if player.value>=2000:
        move="call"

    return move
