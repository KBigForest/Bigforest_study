import random as rd
def card_game():
    card_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    card_suit = ["♠", "♥", "♣", "◆"]
    rd.shuffle(card_suit)
    print(card_suit)
    print('초기 카드 생성')
    for i in card_suit:
        for j in card_number:
            print(f'({i}, {j})', end = '')
        print()
        
    rd.shuffle(card_suit)
    rd.shuffle(card_number)
    card = []
    for i in card_suit:
        for j in card_number:
            card.append((i,j))
    rd.shuffle(card)
    print('Shuffle card')
    for i in range(0,len(card)):
        print(card[i], end ='')
        if (i+1) % 13 == 0:
            print() 
    print('Dealing three cards')
    
    player1 = card[0:3]
    player2 = card[10:13]
    
    
    
    print(player1)
    print(player2)
    player1_total_score = 0
    for i in range(0,3):    
        if player1[i][0] == "♠":
            pattern = 3
        elif player1[i][0] == "♥":
            pattern = 1
        elif player1[i][0] == "♣":
            pattern = 4
        elif player1[i][0] == "◆":
            pattern = 2
        player1_total_score += pattern * player1[i][1]

    player2_total_score = 0
    for i in range(0,3):    
        if player2[i][0] == "♠":
            pattern = 3
        elif player2[i][0] == "♥":
            pattern = 1
        elif player2[i][0] == "♣":
            pattern = 4
        elif player2[i][0] == "◆":
            pattern = 2
        player2_total_score += pattern * player2[i][1]
    print(f'player1 : {player1_total_score}, player2 : {player2_total_score}')
    if player1_total_score > player2_total_score:
        print('player1 win')
    elif player1_total_score < player2_total_score:
        print('player2 win')
    else:
        print('draw')
        
card_game()


