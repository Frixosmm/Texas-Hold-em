# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 12:00:54 2021

@author: Sir Fox
"""

class Player(object):
    name = ""
    money = 0
    bid = 0
    turn=0
    cards=[(0,0),(0,0)]
    value=0
    # The class "constructor" - It's actually an initializer
    def __init__(self, name, money, bid, turn,cards,value):
        self.name = name
        self.money = money
        self.bid = bid
        self.turn=turn
        self.cards=cards
        self.value=value
def make_player(name, money, bid,turn,cards):
    player = Player(name, money, bid,turn,cards,0)
    return player






