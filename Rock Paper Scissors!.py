def rps(p1, p2):
    #your code here
    if p1 != p2:
        if p1=='rock' and p2=='scissors':
            return 'Player 1 won!' 
        elif p1=='paper' and p2=='scissors':
            return 'Player 1 won!' 
        elif p1=='paper' and p2=='rock':
            return 'Player 2 won!' 
        else:
            return None
    else:
        return "Draw!"