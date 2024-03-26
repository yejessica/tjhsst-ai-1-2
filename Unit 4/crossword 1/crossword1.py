import sys ;args = sys.argv[1:]

#Jessica Ye
#2/25/2022


import re, random

BLOCKCHAR = '#'
OPENCHAR = '-'
PROTECTEDCHAR = '~'

def initialize(prefilled_word_dict, height, width):
    xword = '-'*(height*width)
    print(prefilled_word_dict)
    for t in prefilled_word_dict:
        beginning = int(int(t[2])*width + int(t[3]))
        word = t[0][4:]
            
        counter = beginning
        if t[1] == 'V' or t[1] == 'v': #GOING VERTICAL

            for i in range(len(word)):
                # xword[counter] = word[i]
                xword = xword[:counter] + word[i] + xword[counter + 1:]
                counter+=width
            
            # pass
        else: #HORIZONTAL
            for i in range(len(word)):
                # xword[counter] = word[i]
                xword = xword[:counter] + word[i] + xword[counter + 1:]
                counter+=1

  
    return xword
    # display(xword, width)
    # pass

def display(xword, width, height):
    print('\n'.join([xword[width*k:width*(k+1)] for k in range(height)]), end='\n\n')

def create_board(prefilled_word_dict, height, width, num_of_block_goal):
    xword = initialize(prefilled_word_dict, height, width)
    display(xword, width, height)
    print("After adding given words:")
    newBoard = xword
    for i in range(len(xword)-1):
        if xword[i] != '-':
            if xword[i] != '#' and xword[i] != '~':
                newBoard = newBoard[:i] + '~' + newBoard[i+1:]
    newBoard = create_palindrome(newBoard, height, width)
    if num_of_block_goal%2 == 1:
        newBoard = newBoard[:len(newBoard)//2] + '#' + newBoard[len(newBoard)//2+1:]
    else:
        newBoard = newBoard[:len(newBoard)//2] + '~' + newBoard[len(newBoard)//2+1:]

    display(newBoard, width, height)
    word, length = isValid(newBoard, height, width)
    display(word, width, height)
    # print(num_of_block_goal)
    return word

def add_blocks(board, num_of_block_goal, height, width, pos_list, countBlocked):
    # countBlocked = 0

    print(pos_list)
    
    randomPlace = random.choice(pos_list)
    print(randomPlace)
    newBoard = board[:randomPlace] + '#' + board[randomPlace+1:]
    display(newBoard, width, height)
    ifValid, length = isValid(newBoard, height, width)

    if ifValid == 'FALSE':
        newBoard = board
    else:
        print(len(newBoard)+(randomPlace*-1)-1)
        # if (randomPlace*-1)-1 in pos_list:
        newBoard = create_palindrome(newBoard, height, width)
        palindromeValid, length = isValid(newBoard, height, width)
        if palindromeValid == 'FALSE':
            newBoard = board
            
        else:
            if (len(newBoard)+(randomPlace*-1)-1) in pos_list:
                pos_list.remove(len(newBoard)+(randomPlace*-1)-1)
            countBlocked+=2
            display(newBoard, width, height)
            if countBlocked==num_of_block_goal:
                return "hi"
    pos_list.remove(randomPlace)
    add_blocks(newBoard, num_of_block_goal, height, width, pos_list, countBlocked)

    pass

# def add_blocks(xword, block_count, height, width):
def make_pos_list(board, height, width):
    pos_list = [i for i in range(len(board)) if board[i]=='-']
    # print(pos_list)
    return pos_list

def create_palindrome(xword, height, width):
    # middle = (len(xword)/2-1) if (len(xword)%2 == 0) else (len(xword)//2)
    # finalWord1 = xword[:middle] + xword[:middle][::-1]
    newBoard = xword
    for i in range(len(xword)):
        if newBoard[i] != '-':
            urNum = i*-1-1
            # print(urNum)
            if urNum == -1:
                newBoard = newBoard[:urNum] + newBoard[i]
            else:
                newBoard = newBoard[:urNum] + newBoard[i] + newBoard[urNum+1:]
            # print("hi",newBoard)
    return newBoard

    
def isValid(board, height, width): #add NUM??

    xw = BLOCKCHAR*(width+3) + (BLOCKCHAR*2).join([board[p:p+width] for p in range(0, len(board), width)]) + BLOCKCHAR*(width+3)
    illegalRE = "[{}](.?[{}]|[{}].?)[{}]".format(BLOCKCHAR, PROTECTEDCHAR, PROTECTEDCHAR, BLOCKCHAR)
    newH = len(xw) // (width+2)

    for turn in range(2):
        if re.search(illegalRE, xw): return 'FALSE', len(board)
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH

    subRE = "[{}]{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, BLOCKCHAR)
    subRE2 = "[{}]{}{}(?=[{}])".format(BLOCKCHAR, OPENCHAR, OPENCHAR, BLOCKCHAR)
    subRE3 = "[#](-~-|--~|~--|~~-|-~~|~-~)(?=[#])"
    newH = len(xw) // (width+2)

    for turn in range(2):
        xw = re.sub(subRE, BLOCKCHAR*2, xw)
        xw = re.sub(subRE2, BLOCKCHAR*3, xw)
        xw = re.sub(subRE3, BLOCKCHAR+PROTECTEDCHAR*3, xw)
        xw = transpose(xw, len(xw) // newH)
        newH = len(xw) // newH
    new_board = ""

    for row in range(width+2, len(xw)-(width+2), width+2): new_board += xw[row+1:width+row+1]
    return new_board, new_board.count(BLOCKCHAR)
    # pass

def transpose(xw, newWidth):
    return "".join([xw[col::newWidth] for col in range(newWidth)])


#check connectivity of all open chars at the end
def area_fill(board, sp, width):
    # pass
    dirs = [-1, width, 1, -1*width]
    if sp < 0 or sp >= len(board): return board
    if board[sp] in {OPENCHAR, PROTECTEDCHAR}:
        board = board[0:sp] + '?' + board[sp+1:]
        for d in dirs:
            if d == -1 and sp % width == 0: continue #left edge
            if d == 1 and sp+1 % width == 0: continue #right edge
            board = area_fill(board, sp+d, dirs)
    return board

#after all blocks added, change all protected into open
#add prefilled words back
def clean_protected(xword, prefilled_word_dict):
    pass


def main():
    num_of_block_goal, height, width = 0, 4, 4
    prefilled_words = []
    for arg in args:
        # if os.path.isfile(arg):
        #     continue
        if re.search(r'^\d+$', arg):
            num_of_block_goal = int(arg)
            print(num_of_block_goal)
        elif re.search(r'^\d+x\d+$', arg, re.I):
            x = arg.lower().index('x')
            height = int(arg[0:x])
            width = int(arg[x+1:])
        elif re.search(r'^[VH]\d+x\d+.+$', arg, re.I):
            match = re.search(r'^([VH])(\d+)x(\d+)(.+)$', arg, re.I)
            direction, row, col, word_or_block = match.group(0), match.group(1), match.group(2), match.group(3)
            prefilled_words.append((direction, row, col, word_or_block))
    # xword = initialize(prefilled_words, height, width)
    # display(xword, width)
    newBoard = create_board(prefilled_words, height, width, num_of_block_goal)
    pos_list = make_pos_list(newBoard, height, width)
    add_blocks(newBoard, num_of_block_goal, height, width, pos_list, 0)

main()

#Jessica Ye, 5, 2023