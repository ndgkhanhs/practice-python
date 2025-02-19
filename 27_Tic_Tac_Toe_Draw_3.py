def draw_board(game):
    x = (" ---")
    y = ("|   ")
    count = 0
    while count < game:
        print (game*x)
        print (game*y +"|")
        count += 1
        if count == game:
            print (game*x)
            break

def check_win(game):
    #check winner in column and row
    for i in range(3):
        if (game[i][0] == game[i][1] == game[i][2] != " "):
            return game[i][0]
        if (game[0][i] == game[1][i] == game[2][i] != " "):
            return game[0][i]
    #check winner in diagonols
    if (game[0][0] == game[1][1] == game[2][2] != " "):
        return game[0][0]
    if (game[0][2] == game[1][1] == game[2][0] != " "):
        return game[0][2]
    
    return None
        
def ttt():
    game = [[" " for _ in range(3)] for _ in range(3)]
    print(draw_board(game))
    while True:
        winner = check_win(game)
        if winner:
            print("Player", winner, "win")
            break

if "__main__" == __name__:
    ttt()

