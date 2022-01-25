import math
import random
import itertools
from Draw_cards import Draw_cards
from Value_cards import Value_cards
from Best_cards import Best_cards
from Players import make_player
# tcards=[(13,1),(13,2),(13,3),(13,4),(6,1)]

# played_cards=Draw_cards(7)

# a=Best_cards(played_cards)
# print(a[1])
# print(a)
small_blind = 10
big_blind = small_blind * 2
starting_money = big_blind * 10  # chosen arbitrarily
pot = 0
number_of_players = 5
A = [starting_money, 0]
players = A * number_of_players
playing_cards = Draw_cards(5 + 2 * number_of_players)
# print("playing cards are")
# print(playing_cards)
table_cards = playing_cards[0:5]
# print("table cards are")
# print(table_cards)
k = 5
for i in range(0, number_of_players):  # deal cards

    players[(i * len(A)) + 1] = playing_cards[k:k + 2]
    k = k + 2
####################################

# tempo=players[1]
# tempo.extend(table_cards)
# print(tempo) ###tempo contains 7 cards available to player

#################New Game###########################


# TODO# Create players and assign starting states in a scalable way
p0 = make_player("Dealer", starting_money, 0, 2, players[1])
p1 = make_player("Small", starting_money - small_blind, small_blind, 3, players[3])
p2 = make_player("Big", starting_money - big_blind, big_blind, 4, players[5])
p3 = make_player("Busra", starting_money, 0, 0, players[7])
p4 = make_player("Frixos", starting_money, 0, 1, players[9])
participant = []
participant.append(p0)
participant.append(p1)
participant.append(p2)
participant.append(p3)
participant.append(p4)
################stage=0="pre-flop"################################
pot = pot + small_blind + big_blind
highest_bid = big_blind
turns_left = number_of_players - 1
i = 2
while (turns_left >= 0):

    if i == number_of_players - 1:  # i is pointing towards the player who is "speaking" next
        i = 0
    else:
        i = i + 1

    if participant[i].turn == -1:
        turns_left = turns_left - 1
        print(participant[i].name, "has no money or has folded")
    else:
        print(participant[i].name, "has", participant[i].money, "has bid", participant[i].bid, "pot is ", pot,
              ".Calling for:", highest_bid - participant[i].bid)

        move_input = input("Enter your move: ")

        if move_input == "fold":
            participant[i].turn = -1  # wont play anymore
            turns_left -= 1  # progres normally

        elif move_input == "call":
            pot = pot + highest_bid - participant[i].bid

            participant[i].money = participant[i].money - highest_bid + participant[i].bid

            participant[i].bid = highest_bid  # bid change must be last

            turns_left -= 1  # normal
            # print("highest bid is",highest_bid)
            # print(participant[i].name,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

        elif move_input == "raise":
            # call first
            participant[i].money = participant[i].money - highest_bid + participant[i].bid
            pot = pot + highest_bid - participant[i].bid
            participant[i].bid = highest_bid
            #
            raise_amount_input = input("Enter your raise amount: ")
            raise_amount = int(raise_amount_input)

            if raise_amount < participant[i].money:  # <= then includes all in case
                turns_left = number_of_players - 1  # raise count resets

                participant[i].money = participant[i].money - raise_amount
                participant[i].bid = participant[i].bid + raise_amount

                pot = pot + raise_amount
                highest_bid = participant[i].bid
                # print("highest bid is",highest_bid)

                # print("player",i,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

            else:
                print("You dont have enough money!")

        elif move_input == "check":
            turns_left -= 1  # raise count progresses normaly
            if participant[i].bid == highest_bid:
                print("Ckeck")
            else:
                print("You cant really check right now. You fucked up the game")
        elif move_input == "all-in":
            turns_left += number_of_players - 1
        else:
            print("The move input must be call,raise,fold or all-in.Please try again.")
            i=i-1
################stage=0="pre-flop"################################


################stage=1="flop"################################
print("Pre-flop ended, pot is:", pot)
print("Table cards are:",table_cards[0:3])
turns_left = number_of_players - 1
i=0 # small blind plays (we set 0 cause while loop adds one at beginning)
while (turns_left >= 0):

    if i == number_of_players - 1:  # i is pointing towards the player who is "speaking" next
        i = 0
    else:
        i = i + 1

    if participant[i].turn == -1:
        turns_left = turns_left - 1
        print(participant[i].name, "has no money or has folded")
    else:
        print(participant[i].name, "has", participant[i].money, "has bid", participant[i].bid, "pot is ", pot,
              ".Calling for:", highest_bid - participant[i].bid)

        move_input = input("Enter your move: ")

        if move_input == "fold":
            participant[i].turn = -1  # wont play anymore
            turns_left -= 1  # progres normally

        elif move_input == "call":
            pot = pot + highest_bid - participant[i].bid

            participant[i].money = participant[i].money - highest_bid + participant[i].bid

            participant[i].bid = highest_bid  # bid change must be last

            turns_left -= 1  # normal
            # print("highest bid is",highest_bid)
            # print(participant[i].name,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

        elif move_input == "raise":
            # call first
            participant[i].money = participant[i].money - highest_bid + participant[i].bid
            pot = pot + highest_bid - participant[i].bid
            participant[i].bid = highest_bid
            #
            raise_amount_input = input("Enter your raise amount: ")
            raise_amount = int(raise_amount_input)

            if raise_amount < participant[i].money:  # <= then includes all in case
                turns_left = number_of_players - 1  # raise count resets

                participant[i].money = participant[i].money - raise_amount
                participant[i].bid = participant[i].bid + raise_amount

                pot = pot + raise_amount
                highest_bid = participant[i].bid
                # print("highest bid is",highest_bid)

                # print("player",i,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

            else:
                print("You dont have enough money!")

        elif move_input == "check":
            turns_left -= 1  # raise count progresses normaly
            if participant[i].bid == highest_bid:
                print("Ckeck")
            else:
                print("You cant really check right now. You fucked up the game")
        elif move_input == "all-in":
            turns_left += number_of_players - 1
        else:
            print("The move_input must be call,raise,fold or all-in")
################stage=1="flop"################################

################stage=2="turn"################################
print("Flop ended, pot is:", pot)
print("Table cards are:",table_cards[0:4])
turns_left = number_of_players - 1
i=0 # small blind plays (we set 0 cause while loop adds one at beginning)
while (turns_left >= 0):

    if i == number_of_players - 1:  # i is pointing towards the player who is "speaking" next
        i = 0
    else:
        i = i + 1

    if participant[i].turn == -1:
        turns_left = turns_left - 1
        print(participant[i].name, "has no money or has folded")
    else:
        print(participant[i].name, "has", participant[i].money, "has bid", participant[i].bid, "pot is ", pot,
              ".Calling for:", highest_bid - participant[i].bid)

        move_input = input("Enter your move: ")

        if move_input == "fold":
            participant[i].turn = -1  # wont play anymore
            turns_left -= 1  # progres normally

        elif move_input == "call":
            pot = pot + highest_bid - participant[i].bid

            participant[i].money = participant[i].money - highest_bid + participant[i].bid

            participant[i].bid = highest_bid  # bid change must be last

            turns_left -= 1  # normal
            # print("highest bid is",highest_bid)
            # print(participant[i].name,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

        elif move_input == "raise":
            # call first
            participant[i].money = participant[i].money - highest_bid + participant[i].bid
            pot = pot + highest_bid - participant[i].bid
            participant[i].bid = highest_bid
            #
            raise_amount_input = input("Enter your raise amount: ")
            raise_amount = int(raise_amount_input)

            if raise_amount < participant[i].money:  # <= then includes all in case
                turns_left = number_of_players - 1  # raise count resets

                participant[i].money = participant[i].money - raise_amount
                participant[i].bid = participant[i].bid + raise_amount

                pot = pot + raise_amount
                highest_bid = participant[i].bid
                # print("highest bid is",highest_bid)

                # print("player",i,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

            else:
                print("You dont have enough money!")

        elif move_input == "check":
            turns_left -= 1  # raise count progresses normaly
            if participant[i].bid == highest_bid:
                print("Ckeck")
            else:
                print("You cant really check right now. You fucked up the game")
        elif move_input == "all-in":
            turns_left += number_of_players - 1
        else:
            print("The move_input must be call,raise,fold or all-in")
################stage=2="turn"################################

################stage=3="river"################################
print("Turn ended, pot is:", pot)
print("Table cards are:",table_cards[0:5])
turns_left = number_of_players - 1
i=0 # small blind plays (we set 0 cause while loop adds one at beginning)
while (turns_left >= 0):

    if i == number_of_players - 1:  # i is pointing towards the player who is "speaking" next
        i = 0
    else:
        i = i + 1

    if participant[i].turn == -1:
        turns_left = turns_left - 1
        print(participant[i].name, "has no money or has folded")
    else:
        print(participant[i].name, "has", participant[i].money, "has bid", participant[i].bid, "pot is ", pot,
              ".Calling for:", highest_bid - participant[i].bid)

        move_input = input("Enter your move: ")

        if move_input == "fold":
            participant[i].turn = -1  # wont play anymore
            turns_left -= 1  # progres normally

        elif move_input == "call":
            pot = pot + highest_bid - participant[i].bid

            participant[i].money = participant[i].money - highest_bid + participant[i].bid

            participant[i].bid = highest_bid  # bid change must be last

            turns_left -= 1  # normal
            # print("highest bid is",highest_bid)
            # print(participant[i].name,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

        elif move_input == "raise":
            # call first
            participant[i].money = participant[i].money - highest_bid + participant[i].bid
            pot = pot + highest_bid - participant[i].bid
            participant[i].bid = highest_bid
            #
            raise_amount_input = input("Enter your raise amount: ")
            raise_amount = int(raise_amount_input)

            if raise_amount < participant[i].money:  # <= then includes all in case
                turns_left = number_of_players - 1  # raise count resets

                participant[i].money = participant[i].money - raise_amount
                participant[i].bid = participant[i].bid + raise_amount

                pot = pot + raise_amount
                highest_bid = participant[i].bid
                # print("highest bid is",highest_bid)

                # print("player",i,"has",participant[i].money,"has bid",participant[i].bid,"pot is ",pot)

            else:
                print("You dont have enough money!")

        elif move_input == "check":
            turns_left -= 1  # raise count progresses normaly
            if participant[i].bid == highest_bid:
                print("Ckeck")
            else:
                print("You cant really check right now. You fucked up the game")
        elif move_input == "all-in":
            turns_left += number_of_players - 1
        else:
            print("The move_input must be call,raise,fold or all-in")
################stage=3="river"################################


################give each player the value of his 5 best cards#####

#################################################BAD CODE AFTER THIS#############################################

for p in participant:
    temp1=p.cards.copy()
     #something i dont understand was() happening, the value of cards is changing in original objsects p0,p1 etc.which is not intended. I only wanted to update values
    # had to do with .copy() instead of =https://www.w3schools.com/python/python_lists_copy.asp
    for k in table_cards: #collect table cards + player cards for valuation
        temp1.append(k)
        #print(k)
    if p.turn==-1:
        p.value=-1
    else:
        print("Player",p.name,"has")
        p.cards,p.value=list(Best_cards(temp1)).copy()



