from Value_cards import Value_cards

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)


def Best_cards(cards):
    k=combinations(cards,5) #when played_cards=7 this is 7 choose 5 so we can use it to find the hand with the highest value
    best_value=0
    best_cards=cards[0:5]
    for combo in k:
        temp=Value_cards(combo)
        if temp > best_value:
            best_value=temp
            best_cards=combo
    return best_cards,best_value
