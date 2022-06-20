    
def Value_cards(cards):
    value=0
    # TODO# Value returned cannot be 0. It must atleast be the value of highest card?
    cards_value=[0,0,0,0,0]
    cards_suit=[0,0,0,0,0]
    for x in range(0,5):
        cards_value[x]=cards[x][0]
        cards_suit[x]=cards[x][1]   

    counts_store=[0]*14
    for i in range(1,15): #from 2 to 14 counts how many of "2" or "3" etc there are
        counts_store[i-2]=cards_value.count(i)
                        #if there are only "1"'s there are no pairs
                        #if there is 1 "2" there is couple 
                        #if there is 1 "3" its a three of a kind
                        #if there is 1 "4" its a four of a kind
                        #if there is 1 "2" and 1 "3" there is a full house
                        #if there are 2 "2" and 2 "2" there are two pairs        
    #print(counts_store)
    sorted_cards=sorted(cards_value)

    
 #####################IF ALL CARDS HAVE DIFFERENT VALUES(str,fl,strfl#############       
    if counts_store.count(1)==5:
        straight=False
        flush=False
        if sorted_cards[0]==sorted_cards[1]-1:
            if sorted_cards[0]==sorted_cards[2]-2:
                if sorted_cards[0]==sorted_cards[3]-3:
                    if sorted_cards[0]==sorted_cards[4]-4:
                        straight=True 
                        value=4000
                        value=value+sorted_cards[4]
                        #print("straight")
                        
        if cards_suit[0]==cards_suit[1]==cards_suit[2]==cards_suit[3]==cards_suit[4]:
            #print("flush")
            value=5000
            for i in sorted_cards:
                value=value+i
                
            flush=True
        
        

        if flush==True and straight==True:
            value=8000
            #print("straight flush")
            if cards_value.count(14)==1:
                value=10000
                #print("royal flush! HOLY SHIT!")
    
 #####################MIXED VALUES (all other combos)######################    
    elif counts_store.count(2)==1:
        if counts_store.count(3)==1:
            value=6000
            for i in range (1,15):
                if counts_store[i-1]==3:
                    value=value+i*10   ###the triple is valued higher than double
                elif counts_store[i-1]==2:
                    value=value+i
            #print("full house")
        else:
            value=1000
            for i in range(1,15):
                if counts_store[i-1]==2:
                    value=value+i*10
                elif counts_store[i-1]==1:
                    value=value+i
            #print("one pair")
        
    elif counts_store.count(2)==2:
        #print("two_pairs")
        value=2000
        for i in range(1,15):
            if counts_store[i-1]==2:
                value=value+i*10
            elif counts_store[i-1]==1:
                value=value+i

    elif counts_store.count(3)==1:
        value=3000
        #print("three of a kind")
        for i in range(1,15):
            if counts_store[i-1]==3:
                value=value+i*10
            elif counts_store[i-1]==1:
                value=value+i
    
    elif counts_store.count(4)==1:
        value=7000
        #print("four of a kind")
        for i in range(1,15):
            if counts_store[i-1]==4:
                value=value+i*10
            elif counts_store[i-1]==1:
                value=value+i
    return value
