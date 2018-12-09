import random 
import time
p1='Player'
board=[1,2,3,4,5,6,7,8,9]
board1=[1,2,3,4,5,6,7,8,9]
select='y'
def show():
    print('-------------')
    print('|',board[0],'|',board[1],'|',board[2],'|')
    print('|',' ','|',' ','|',' ','|')
    print('-------------')
    print('|',board[3],'|',board[4],'|',board[5],'|')
    print('|',' ','|',' ','|',' ','|')
    print('-------------')
    print('|',board[6],'|',board[7],'|',board[8],'|')          
    print('|',' ','|',' ','|',' ','|')
    print('-------------')
def cpu_move(sym1,sym2):
    if((board[0]==board[4]==sym2) and board[8]!=sym1):
        return 9
    elif((board[0]==board[8]==sym2) and board[4]!=sym1):
        return 5
    elif((board[8]==board[4]==sym2) and board[0]!=sym1):
        return 1     
    elif((board[2]==board[4]==sym2) and board[6]!=sym1):
        return 7
    elif((board[2]==board[6]==sym2) and board[4]!=sym1):
        return 5
    elif((board[4]==board[6]==sym2) and board[2]!=sym1):
        return 3
    elif((board[0]==board[3]==sym2) and board[6]!=sym1):
        return 7
    elif((board[0]==board[6]==sym2) and board[3]!=sym1):
        return 4
    elif((board[3]==board[6]==sym2) and board[0]!=sym1):
        return 1
    elif((board[1]==board[4]==sym2) and board[7]!=sym1):
        return 8
    elif((board[1]==board[7]==sym2) and board[4]!=sym1):
        return 5
    elif((board[4]==board[7]==sym2) and board[1]!=sym1):
        return 2
    elif((board[5]==board[8]==sym2) and board[2]!=sym1):
        return 3
    elif((board[2]==board[8]==sym2 and board[5]!=sym1)):
        return 6
    elif((board[2]==board[5]==sym2) and board[8]!=sym1):
        return 9
    elif((board[1]==board[2]==sym2) and board[0]!=sym1):
        return 1
    elif((board[0]==board[2]==sym2) and board[1]!=sym1):
        return 2
    elif((board[0]==board[1]==sym2) and board[2]!=sym1):
        return 3
    elif((board[4]==board[5]==sym2) and board[3]!=sym1):
        return 4
    elif((board[3]==board[5]==sym2) and board[4]!=sym1):
        return 5
    elif((board[3]==board[4]==sym2) and board[5]!=sym1):
        return 6
    elif((board[7]==board[8]==sym2) and board[6]!=sym1):
        return 7
    elif((board[6]==board[8]==sym2) and board[7]!=sym1):
        return 8
    elif((board[6]==board[7]==sym2) and board[8]!=sym1):
        return 9
    elif((board[0]==board[4]==sym1) and board[8]!=sym2):
        return 9
    elif((board[0]==board[8]==sym1) and board[4]!=sym2):
        return 5
    elif((board[8]==board[4]==sym1) and board[0]!=sym2):
        return 1     
    elif((board[2]==board[4]==sym1) and board[6]!=sym2):
        return 7
    elif((board[2]==board[6]==sym1) and board[4]!=sym2):
        return 5
    elif((board[4]==board[6]==sym1) and board[2]!=sym2):
        return 3
    elif((board[0]==board[3]==sym1) and board[6]!=sym2):
        return 7
    elif((board[0]==board[6]==sym1) and board[3]!=sym2):
        return 4
    elif((board[3]==board[6]==sym1) and board[0]!=sym2):
        return 1
    elif((board[1]==board[4]==sym1) and board[7]!=sym2):
        return 8
    elif((board[1]==board[7]==sym1) and board[4]!=sym2):
        return 5
    elif((board[4]==board[7]==sym1) and board[1]!=sym2):
        return 2
    elif((board[5]==board[8]==sym1) and board[2]!=sym2):
        return 3
    elif((board[2]==board[8]==sym1 and board[5]!=sym2)):
        return 6
    elif((board[2]==board[5]==sym1) and board[8]!=sym2):
        return 9
    elif((board[1]==board[2]==sym1) and board[0]!=sym2):
        return 1
    elif((board[0]==board[2]==sym1) and board[1]!=sym2):
        return 2
    elif((board[0]==board[1]==sym1) and board[2]!=sym2):
        return 3
    elif((board[4]==board[5]==sym1) and board[3]!=sym2):
        return 4
    elif((board[3]==board[5]==sym1) and board[4]!=sym2):
        return 5
    elif((board[3]==board[4]==sym1) and board[5]!=sym2):
        return 6
    elif((board[7]==board[8]==sym1) and board[6]!=sym2):
        return 7
    elif((board[6]==board[8]==sym1) and board[7]!=sym2):
        return 8
    elif((board[6]==board[7]==sym1) and board[8]!=sym2):
        return 9
    else:
         while(True):   
             cpu_spot=random.randint(1,9)   
             if(board[cpu_spot-1]!=sym1 and board[cpu_spot-1]!=sym2 and (cpu_spot in board1)):
                 return cpu_spot
             else:
                 continue
             
         
         
def result(sym1,sym2):
    if((board[0]==board[4]==board[8]==sym1)):
        return 1
    elif((board[0]==board[4]==board[8]==sym2)):    
        return 2
    elif((board[2]==board[4]==board[6]==sym1)):
        return 1
    elif((board[2]==board[4]==board[6]==sym2)):
        return 2             
    elif((board[0]==board[1]==board[2]==sym1)):  
        return 1        
    elif((board[3]==board[4]==board[5]==sym1)):  
        return 1
    elif((board[6]==board[7]==board[8]==sym1)):
        return 1
    elif((board[0]==board[3]==board[6]==sym1)):
        return 1
    elif((board[1]==board[4]==board[7]==sym1)):
        return 1
    elif((board[2]==board[5]==board[8]==sym1)):  
        return 1
    elif((board[0]==board[1]==board[2]==sym2)):  
        return 2        
    elif((board[3]==board[4]==board[5]==sym2)): 
        return 2
    elif((board[6]==board[7]==board[8]==sym2)):
        return 2
    elif((board[0]==board[3]==board[6]==sym2)):
        return 2
    elif((board[1]==board[4]==board[7]==sym2)):
        return 2
    elif((board[2]==board[5]==board[8]==sym2)):
        return 2
    else:
        return 0
def title():
    print('======================================================================================')
    print('||  _________  _________     ____    _______   _        ___   _______        _____  ||')
    print('||      |          |        /           |     / \      /         |    ___   |       ||')
    print('||      |          |       /            |    /   \    /          |   /   \  |____   ||')
    print('||      |          |      |      ===    |   /-----\  |     ===   |  |     | |       ||') 
    print('||      |          |       \            |  /       \  \          |  |     | |       ||')
    print('||      |      ____|_____   \____       | /         \  \___      |   \___/  |_____  ||')
    print('||                                                                                  ||')          
    print('======================================================================================')

    
list=['O','X']
title()
print("\n\n\n!!!Welome to the game of Tic-Tac-Toe!!!")
print('This is a Player 1 V/S CPU game....')

while(True):
    print('Whom you want to give first turn: CPU or Player1?')
    turn=input('Your choice: ')
    turn=turn.upper()
    if(turn=='PLAYER 1' or turn=='PLAYER1' or turn=='CPU' or turn=='C P U' or turn=='C.P.U'):
        p1=input("Enter Player 1's name: ")
        print('Player 1 name added successfully...')
        break
    else:
        print('Invaild choice!!!')
        print('Retry again....')
        continue
    
while(select=='y' or select=='Y'):
    while(True):
        sym1=input('Select symbol for {} from O or X:\t'.format(p1))
        sym1=sym1.upper()
        if(sym1=='O' or sym1=='X'):
            list.remove(sym1)
            sym2=list[0]
            print("{}'s symbol is now".format(p1),sym1)
            print("CPU's symbol is now",sym2)
            break
        else:
            print('Invalid selection!!!')
            print('Try again....')
            continue
    print('Loading Tic-Tac-Toe Board....')
    print('Please Wait...')
    for i in range(2):
        time.sleep(2.5)
    for i in range(10):
        print(10-i,'seconds remaining....')
        time.sleep(1)
    print('Tic-Tac-Toe board loaded succssfully.....')      
    print('Press enter key to generate the board on screen......')
    input()
    show()
    print('Nice Job!')
    print('Now press enter key to start the game......')
    input()
    res=-1
    if(turn=='PLAYER 1' or turn=='PLAYER1'):
        while(True):
            print('Select any position for placing your symbol on board (From 1-9).')
            spot1=int(input("{}'s turn:".format(p1)))
            if((spot1 in board) and board[spot1-1]!=sym2):
                board[spot1-1]=sym1
                show()
                board1.remove(spot1)

            else:
                print('Position not available....')
                print('Retry again......')
                continue
            res=result(sym1,sym2)
            if(res!=0):
                break
            if(board1==[]):
                break
            print("CPU's turn:")
            for i in range(2):
                time.sleep(2.5)
            cpu_spot=cpu_move(sym1,sym2)
            board[cpu_spot-1]=sym2
            board1.remove(cpu_spot)
            res=result(sym1,sym2)
            show()
            if(res!=0):
                break
    if(turn=='CPU' or turn=='C P U' or turn=='C.P.U'):
        while(True):
            print("CPU's turn:")
            for i in range(2):
                time.sleep(2.5)
            cpu_spot=cpu_move(sym1,sym2)
            board[cpu_spot-1]=sym2
            board1.remove(cpu_spot)
            res=result(sym1,sym2)
            show()
            if(res!=0):
                break
            if(board1==[]): break
            while(True):
                print('Select any position for placing your symbol on board (From 1-9).')
                spot1=int(input("{}'s turn:".format(p1)))
                if((spot1 in board) and board[spot1-1]!=sym2):
                    board[spot1-1]=sym1
                    show()
                    board1.remove(spot1)
                    break;

                else:
                    print('Position not available....')
                    print('Retry again......')
                    continue
            res=result(sym1,sym2)
            if(res!=0):
                break
            if(board1==[]):
                break
    if(res==1):
        print('Game is finished!!!')
        print('Hit enter key to generate the result:')
        input()
        print('{} wins the game'.format(p1))
        print('Congratulations to {}.....'.format(p1))
        print('See you next time...')
        print('Alvida...')
        print('Thank you for playing the game...')
    elif(res==2):
        print('Game is finished!!!')
        print('Hit enter key to generate the result:')
        input()
        print('CPU wins the game')
        print('Better luck next time {}'.format(p1))
        print('See you next time...')
        print('Alvida...')
        print('Thank you for playing the game...')
    else:
        print('Game is finished!!!')
        print("Draw Match!!!!")
        print("Winner cannot be decided")
        print('See you next time...')
        print('Alvida...')
        print('Thank you for playing the game...')
    while(True):
        print('Want to play the game again?(y/n)')
        select=input('Your choice: ')
        if(select=='y' or select=='Y'):
            break
        elif(select=='n' or select=='N'):
            time.sleep(1)
            print('.......GAME OVER.......')
            break
        else:
            print('Invalid choice...')
            print('Retry again...')
            continue

print('\n')
print('Game Credits:\n')
print('Coded and Designed by:','Anurag Dev')
print('References:','Google(The God)')
input()
      


    
