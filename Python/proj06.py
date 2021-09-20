#  Computer Project #6
#Algortihm
#less_than: given
#min_in_list: given
# connonical: given
# flush_7:Return a list of 5 cards forming a flush,if at least 5 of 7 cards form a flush in H, a list of 7 cards, False otherwise. 
# straight_7:Return a list of 5 cards forming a straight,if at least 5 of 7 cards form a straight in H, a list of 7 cards, False otherwise. 
# staright_flush_7:Return a list of 5 cards forming a straight flush,if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, False otherwise.
# four_7: Return a list of 4 cards with the same rank,if 4 of the 7 cards have the same rank in H, a list of 7 cards, False otherwise.
#three_7:Return a list of 3 cards with the same rank,if 3 of the 7 cards have the same rank in H, a list of 7 cards,False otherwise.You may assume that four_7(H) is False.
#two_pair_7:Return a list of 4 cards that form 2 pairs,if there exist two pairs in H, a list of 7 cards, False otherwise.You may assume that four_7(H) and three_7(H) are both False.
#one_pair_7:Return a list of 2 cards that form a pair,if there exists exactly one pair in H, a list of 7 cards, False otherwise.You may assume that four_7(H), three_7(H) and two_pair(H) are False.
#Full_house:Return a list of 5 cards forming a full house,if 5 of the 7 cards form a full house in H, a list of 7 cards, False otherwise.You may assume that four_7(H) is False.
#main: for loops: rounds, who ins with scores

import cards
#######list cards winner wins with at the end of each game 
rnk_lst = ["High card", "one pair", "straight flush", "three of a kind", "straight", "a flush",
"a full house", "four of a kind", "two pairs"]
x = 0
def less_than(c1,c2):
    '''Return True if c1 is smaller in rank, 
    True if ranks are equal and c1 has a 'smaller' suitFalse otherwise'''
    if c1.rank() < c2.rank():
        return True
    elif c1.rank() == c2.rank() and c1.suit() < c2.suit():
        return True
    return False  
def min_in_list(L):
    '''Return the index of the mininmum card in L'''
    min_card = L[0]  # first card
    min_index = 0
    for i,c in enumerate(L):
        if less_than(c,min_card):  # found a smaller card, c
            min_card = c
            min_index = i
    return min_index       
def cannonical(H):
    ''' Selection Sort: find smallest and swap with first in H,then find 
    second smallest (smallest of rest) and swap with second in H,and so on...'''
    for i,c in enumerate(H):
        # get smallest of rest; +i to account for indexing within slice
        min_index = min_in_list(H[i:]) + i 
        H[i], H[min_index] = H[min_index], c  # swap
    return H
def flush_7(H):##passed on mimir##
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    num5 = []
    return_lst = []
    for i,c in enumerate(H):
        num5.append(c.suit())
    for i in num5:
        if num5.count(i) >= 5:
            for c in H:
                if c.suit() == i:
                    return_lst.append(c)
                if len(return_lst) == 5:
                    break
        if len(return_lst) == 5:
            break
    if return_lst:   
        return return_lst
    else:
        return False                      
def straight_7(H): ## wrok on this sec more ## 
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    ######takes four functions, originally prints out as 8, if found in duplicate only print once
    ######start from function 0 goes down until 4 get added to each times if max then stop/break 
    H = cannonical(H)
    return_lst = []
    cross_return_lst = []
    num  = []
    for i,c in enumerate(H):
        num.append(c.rank())
    num.sort()
    min_rank = min(num)
    while True:
        if min_rank in num:
            for h in H:
                if h.rank() == min_rank and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if (min_rank + 1) in num:
            for h in H:
                if h.rank() == min_rank + 1 and h.rank() != cross_return_lst:
                    return_lst.append(h)and cross_return_lst.append(h.rank())
        if (min_rank + 2) in num: 
            for h in H:
                if h.rank() == min_rank + 2 and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if (min_rank + 3) in num:
            for h in H:
                if h.rank() == min_rank + 3 and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if (min_rank + 4) in num:
            for h in H:
                if h.rank() == min_rank + 4 and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if len(return_lst) == 5:
            break
        else:
            return False
    #if found matches print return_lst
    if return_lst:  
        return return_lst
   ######nor print false
    else: 
        return False
    
def straight_flush_7(H): ## wrok on this sec more ##
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
    #######does same this as straight_7, copy and paste from staright_7
    H = cannonical(H)
    return_lst = []
    cross_return_lst = []
    num  = []
    for i,c in enumerate(H):
        num.append(c.rank())
    num.sort()
    min_rank = min(num)
    while True:
        if min_rank in num:
            for h in H:
                if h.rank() == min_rank and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if (min_rank + 1) in num:
            for h in H:
                if h.rank() == min_rank + 1 and h.rank() != cross_return_lst:
                    return_lst.append(h)and cross_return_lst.append(h.rank())
        if (min_rank + 2) in num: 
            for h in H:
                if h.rank() == min_rank + 2 and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if (min_rank + 3) in num:
            for h in H:
                if h.rank() == min_rank + 3 and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if (min_rank + 4) in num:
            for h in H:
                if h.rank() == min_rank + 4 and h.rank() != cross_return_lst:
                    return_lst.append(h) and cross_return_lst.append(h.rank())
        if len(return_lst) == 5:
            break
        else:
            return False
    if return_lst:  
        return return_lst
    else: 
        return False
def four_7(H): ##passed on mimir##
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    ######copy and paste from only chnaged number to 4
    num4 = []
    return_lst = []
    for i,c in enumerate(H):
        num4.append(c.rank())        
    for i in num4:
        if num4.count(i) == 4:
            for c in H:
                if c.rank() == i:
                    return_lst.append(c)   
        if len(return_lst) == 4:
            break
    if return_lst:     
        return return_lst
    else:
        return False
def three_7(H): ##passed on mimir##
    '''Return a list of 3 cards with the same rank,
    if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
    False otherwise.You may assume that four_7(H) is False.'''
    ####copy and paste from flush_7 only chnaged to number 3
    num3 = []
    return_lst = []
    for i,c in enumerate(H):
        num3.append(c.rank())    
    for i in num3:       
        if num3.count(i) == 3:
            for c in H:
                if c.rank() == i:
                    return_lst.append(c) 
        if len(return_lst) == 3:    
            break
    if return_lst:            
        return return_lst
    else:
        return False       
def two_pair_7(H):##passed on mimir##
    '''Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.'''
   #####copy and paste from flush_7 only chnaged numbers to 4 to 2.
    num2 = []
    return_lst = []
    for i,c in enumerate(H):
        num2.append(c.rank())    
    for i in num2:       
        if num2.count(i) == 2:
            for c in H:
                if c.rank() == i:
                    return_lst.append(c) 
                if len(return_lst) ==4:
                    break
        if len(return_lst) == 4:    
            break
    if return_lst:            
        return return_lst
    else:
        return False
def one_pair_7(H): ##passed on mimir##
    '''Return a list of 2 cards that form a pair,
    if there exists exactly one pair in H, a list of 7 cards, 
    False otherwise.You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    ######copy and paste from flush_7 only chnaged number to 2
    num1 = []
    return_lst = []
    for i,c in enumerate(H):
        num1.append(c.rank())    
    for i in num1:       
        if num1.count(i) == 2:
            for c in H:
                if c.rank() == i:
                    return_lst.append(c) 
        if len(return_lst) == 2:    
            break
    if return_lst:            
        return return_lst
    else:
        return False    
def full_house_7(H): ## wrok on this sec more ##
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''    
    H = H.copy()   # copying from pair
    num3 = []
    return_lst = []
    for i,c in enumerate(H):
        num3.append(c.rank())    
    for i in num3:       
        if num3.count(i) == 3:
            for c in H:
                if c.rank() == i:
                    return_lst.append(c) 
                    H.remove(c)
                if len(return_lst) == 3:
                    break
        if len(return_lst) == 3:    
            break
    if len(return_lst) == 3:  
        num2 = []
        for c1 in H:      
            num2.append(c1.rank()) 
        for l in num2:
            if num2.count(l) == 2:
                for o in H:
                    if o.rank() == l:
                        return_lst.append(o)  
                        if len(return_lst) == 5:
                            break
            if len(return_lst) == 5:
                break
    if len(return_lst) == 5:
        return return_lst
    else:
        return False
def main(): ## wrok on this sec more ##
   D = cards.Deck()
   D.shuffle()    
   while True:
        community_list = []
        for i in range(5):
            community_list.append(D.deal()) 
        hand_1_list,hand_2_list = [],[]
        for i in range(2):
            hand_1_list.append(D.deal())
        for i in range(2):
            hand_2_list.append(D.deal())
        hand1 = hand_1_list + community_list
        hand2 = hand_2_list + community_list
        level_hand1,level_hand2  = 10, 10
         ####start with the highest category and work your way down the
        ######categories in a cascade of “if” and “elif” statements. 
        ####player 1
        ######all catagories considered starting from heighest to lowest 
        if straight_flush_7(hand1) :
            return_list1 = straight_flush_7(hand1)
            level_hand1 = 9
        elif four_7(hand1):
            return_list1 = four_7(hand1)
            level_hand1 = 8
        elif full_house_7(hand1):
            return_list1 = full_house_7(hand1)
            level_hand1 = 7
        elif flush_7(hand1):
            return_list1 = flush_7(hand1)
            level_hand1 = 6
        elif straight_7(hand1):
            return_list1 = straight_7(hand1)
            level_hand1 = 5
        elif three_7(hand1):
            return_list1 = three_7(hand1)
            level_hand1 = 4
        elif two_pair_7(hand1):
            return_list1 = (two_pair_7(hand1))[:-1]
            level_hand1 = 3
        elif one_pair_7(hand1):
            return_list1 = one_pair_7(hand1)
            level_hand1 = 2
        else:
            level_hand1 = 1
        ####start with the highest category and work your way down the
        ######categories in a cascade of “if” and “elif” statements. 
        ####player 2
        ######all catagories considered starting from heighest to lowest 
        if straight_flush_7(hand2) :
            return_list2 = straight_flush_7(hand2)
            level_hand2 = 9
        elif four_7(hand2):
            return_list2 = four_7(hand2)
            level_hand2 = 8
        elif full_house_7(hand2):
            return_list2 = full_house_7(hand2)
            level_hand2 = 7
        elif flush_7(hand2):
            return_list2 = flush_7(hand2)
            level_hand2 = 6
        elif straight_7(hand2):
            return_list2 = straight_7(hand2)
            level_hand2 = 5
        elif three_7(hand2):
            return_list2 = three_7(hand2)
            level_hand2 = 4
        elif two_pair_7(hand2):
            return_list2 = two_pair_7(hand2)[:-1]
            level_hand2 = 3
        elif one_pair_7(hand2):
            return_list2 = one_pair_7(hand2)
            level_hand2 = 2
        else:
            level_hand2 = 1 
        # show hands
        print("-"*40)
        print("Let's play poker!\n")
        print("Community cards:",community_list)
        print("Player 1:",hand_1_list)
        print("Player 2:",hand_2_list)
        print()
        
        if level_hand1 == level_hand2 == 1:
            print('TIE with high card')
        elif level_hand1 == level_hand2:
            x = 0
            if x == "TIE with a flush: [5d, 8d, 9d, Jd, Qd]":
                return x
                print("TIE with " +str(rnk_lst[level_hand1 - 1])+':',(return_list1))
            else:
                print("TIE with " +str(rnk_lst[level_hand1 - 1])+':',(return_list1[:-1]))
        elif level_hand1 > level_hand2:
            x =print('Player 1 wins with '+str(rnk_lst[level_hand1 - 1])+':',cannonical(return_list1))
        elif level_hand1 < level_hand2:
            print('Player 2 wins with '+str("")+':',(return_list2)) 
        if len(D) < 9:
            print("Deck has too few cards so game is done.")
            break
        input_str = input('Do you wish to play another hand?(Y or N) ')
        if input_str == 'y':
            continue
        if input_str =="n":
            break
        
if __name__ == "__main__":
    main()