board_list = ['0','1','2', '3','4','5', '6','7','8']

winx0 = ['X','X','X', '3','4','5', '6','7','8']
winx1 = ['0','1','2', 'X','X','X', '6','7','8']
winx2 = ['0','1','2', '3','4','5', 'X','X','X']
winx3 = ['X','1','2', 'X','4','5', 'X','7','8']
winx4 = ['0','X','2', '3','X','5', '6','X','8']
winx5 = ['0','1','X', '3','4','X', '6','7','X']
winx6 = ['X','1','2', '3','X','5', '6','7','X']
winx7 = ['0','1','X', '3','X','5', 'X','7','8']

wino0 = ['O','O','O', '3','4','5', '6','7','8']
wino1 = ['0','1','2', 'O','O','O', '6','7','8']
wino2 = ['0','1','2', '3','4','5', 'O','O','O']
wino3 = ['O','1','2', 'O','4','5', 'O','7','8']
wino4 = ['0','O','2', '3','O','5', '6','O','8']
wino5 = ['0','1','O', '3','4','O', '6','7','O']
wino6 = ['O','1','2', '3','O','5', '6','7','O']
wino7 = ['0','1','O', '3','O','5', 'O','7','8']


win = False

def win_check():
    if board_list[0] == winx0[0] and board_list[1] == winx0[1] and board_list[2] == winx0[2]:
        return True 
    elif board_list[3] == winx1[3] and board_list[4] == winx1[4] and board_list[5] == winx1[5]:
        return True 
    elif board_list[6] == winx2[6] and board_list[7] == winx2[7] and board_list[8] == winx2[8]:
        return True 
    elif board_list[0] == winx3[0] and board_list[3] == winx3[3] and board_list[6] == winx3[6]:
        return True
    elif board_list[1] == winx4[1] and board_list[4] == winx4[4] and board_list[7] == winx4[7]:
        return True
    elif board_list[2] == winx5[2] and board_list[5] == winx5[5] and board_list[8] == winx5[8]:
        return True
    elif board_list[0] == winx6[0] and board_list[4] == winx6[4] and board_list[8] == winx6[8]:
        return True
    elif board_list[2] == winx7[2] and board_list[4] == winx7[4] and board_list[6] == winx7[6]:
        return True
    elif board_list[0] == wino0[0] and board_list[1] == wino0[1] and board_list[2] == wino0[2]:
        return True 
    elif board_list[3] == wino1[3] and board_list[4] == wino1[4] and board_list[5] == wino1[5]:
        return True 
    elif board_list[6] == wino2[6] and board_list[7] == wino2[7] and board_list[8] == wino2[8]:
        return True 
    elif board_list[0] == wino3[0] and board_list[3] == wino3[3] and board_list[6] == wino3[6]:
        return True
    elif board_list[1] == wino4[1] and board_list[4] == wino4[4] and board_list[7] == wino4[7]:
        return True
    elif board_list[2] == wino5[2] and board_list[5] == wino5[5] and board_list[8] == wino5[8]:
        return True
    elif board_list[0] == wino6[0] and board_list[4] == wino6[4] and board_list[8] == wino6[8]:
        return True
    elif board_list[2] == wino7[2] and board_list[4] == wino7[4] and board_list[6] == wino7[6]:
        return True
    else:
        return False


def board_print():
    print('\n', board_list[0:3], '\n', board_list[3:6], '\n', board_list[6:9])

def playerxinput():
    player_input = input('Player X please enter your move:')
    player_input_int = int(player_input)
    board_list[player_input_int] = 'X'
    print('\n', board_list[0:3], '\n', board_list[3:6], '\n', board_list[6:9])
        
def playeroinput():
    player_input2 = input('Player O please enter your move:')
    player_input_int2 = int(player_input2)
    board_list[player_input_int2] = 'O'
    print('\n', board_list[0:3], '\n', board_list[3:6], '\n', board_list[6:9])
        
x_count = 0       
o_count = 0 
    
while win == False:
    if x_count < o_count:
        board_print()
        playerxinput()
        x_count = x_count + 1
        win = win_check()
    elif o_count < x_count:
        board_print()
        playeroinput()
        o_count = o_count + 1
        win = win_check()
    elif x_count == o_count: 
        board_print()
        playerxinput()
        x_count = x_count + 1
        win = win_check()
else:
        print('You have won!')
