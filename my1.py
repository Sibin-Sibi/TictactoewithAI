board = [' ' for x in range(10)]

def insertboard(letter,pos):
    global board
    board[pos] = letter
    
def spaceisfree(pos):
    return board[pos] == ' '

    
def displayboard(board):
    
 # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

    
def iswinner(le,bo):
    return ((bo[1] == le and bo[2] == le and bo[3] == le ) or (bo[4] == le and bo[5] == le and bo[6] == le ) or (bo[7] == le and bo[8] ==le and bo[9] == le ) or (bo[1] == le and bo[4] == le and bo[7] == le ) or (bo[2] == le and bo[5] == le and bo[8] == le ) or (bo[3] == le and bo[6] ==le and bo[9] == le ) or (bo[1] == le and bo[5] ==le and bo[9] == le ) or (bo[3] == le and bo[5] ==le and bo[7] == le )) 
    
def isboardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True
    
def playermove():
    
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:
                if spaceisfree(move):
                    run = False
                    insertboard('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compmove():
    possiblemoves = [x  for x , letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if iswinner(let,boardcopy):
                move = i
                return move
    # to take the corner.
    opencorners = []
    for i in possiblemoves:
        if i in [1,3,9,7]:
            opencorners.append(i)
    if len(opencorners) > 1:
        move = selectrandom(opencorners)
        return move
    
    # try to take the center
    
    if 5 in possiblemoves:
        move = 5
        return move
    
    openedges = []
    for i in possiblemoves:
        if i in [2,4,6,8]:
            openedges.append(i)
    if len(openedges) > 0:
        move = selectrandom(openedges)
        return move
    
def  selectrandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
        
            
    
    
    
    
def main():
    
    print("welcome to tic tac toe!!!!!!!")
    displayboard(board)
    
    while not(isboardfull(board)):
        if not(iswinner('O',board)):
            playermove()
            displayboard(board)
             
        else:
        
            print("better luck next time.. O is the winner")
            break
        if not(iswinner('X',board)):
            move = compmove()
            if (move == 0):
                print("The game is tied")
            else:
                insertboard('O',move)
                print("The computer placed an 'O' in position :", move) 
            displayboard(board)
        else:
            print("Congratulation.. You Won")
        
            
    if(isboardfull()):
        print("The game is tied")
        
main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break    
