import sys ;args = sys.argv[1:]

#Jessica Ye
#2/25/2022


import re, random

BLOCKCHAR = '#'
OPENCHAR = '-'
PROTECTEDCHAR = '~'

def initialize(prefilled_words, height, width):
    xword = '-'*(height*width)
    # print(prefilled_word_dict)
    for word in prefilled_words:
        direction, r, c, w = word
        w = w.upper()
        if direction.lower() == 'h':
            start = r*width + c
            xword = xword[:start] + w + xword[start+len(w):]
        else:
            xword_list = list(xword)
            for i in range(len(w)):
                xword_list[(r+i)*width + c] = w[i]
            xword = ''.join(xword_list)
        
    return xword
    # display(xword, width)
    # pass

def display(xword, height, width):
    print('\n'.join([xword[width*k:width*(k+1)] for k in range(height)]), end='\n\n')

def add_blocked_squares(board, num, height, width):
    print('h')
    temp_list = []
    for ch in board:
        if ch != BLOCKCHAR and ch != OPENCHAR: temp_list.append(PROTECTEDCHAR)
        else: temp_list.append(ch)
    if height*width % 2 == 1 and num % 2 == 1: temp_list[len(board) // 2] = BLOCKCHAR
    elif height*width % 2 == 1 and num % 2 == 0: temp_list[len(board) // 2] = PROTECTEDCHAR
    new_board = ''.join(temp_list)
    new_board, x = block_helper(new_board, num, height, width)
    if x >= num: return combine(board, new_board)
    new_board, x = make_palindrome(new_board, num, height, width)
    if x >= num: return combine(board, new_board)
    print('After adding given words:')
    display(new_board, height, width)
    pos_list = [x for x in range(len(new_board)) if new_board[x] == OPENCHAR and new_board[len(new_board)-x-1] == OPENCHAR]
    temp_board, x = add_block_helper(new_board, num, height, width, x, pos_list)
    print("hi")
    temp_board, x = block_helper(temp_board, num, height, width)
    # print('hi', temp_board)
    while check_connectivity(temp_board, x, num, height, width) == False or x != num:
        pos_list = [z for z in range(len(new_board)) if new_board[z] == OPENCHAR and new_board[len(new_board)-z-1] == OPENCHAR]
        temp_board, x = add_block_helper(new_board, num, height, width, x, pos_list)
        temp_board, x = block_helper(temp_board, num, height, width)
    board = combine(board, temp_board)
    print("hihihihihi")
    return board

def add_block_helper(board, num, height, width, x, pos_list):
    if x == num: return board, x
    print('pos list is:', pos_list)
    display(board, height, width)
    if len(pos_list) == 0:
        return board, x
    pick = random.randint(0, len(pos_list)-1)
    picked_pos = pos_list[pick]
    pos_list = pos_list[0:pick] + pos_list[pick+1:]
    board = board[0:picked_pos] + BLOCKCHAR + board[picked_pos+1:]

    new_board, x = block_helper(board, num, height, width)
    print("New Board", x)
    display(new_board, height, width)
    if x > num:
        board = board[0:picked_pos] + OPENCHAR + board[picked_pos+1:]
        x = board.count(BLOCKCHAR)
    else:
        new_board, x = make_palindrome(new_board, num, height, width)
        if x > num:
            board = board[0:picked_pos] + OPENCHAR + board[picked_pos+1:]
            x = board.count(BLOCKCHAR)
        else: board = new_board
    pos_list = [z for z in pos_list if board[z] == OPENCHAR]
    return add_block_helper(board, num, height, width, x, pos_list)

def combine(board, new_board):
    nb_list = list(new_board)
    for x in range(len(board)):
        if board[x] not in {BLOCKCHAR, PROTECTEDCHAR, OPENCHAR}:
            nb_list[x] == board[x]
    return ''.join(nb_list)

def cc_helper(b_list, sp, width):
    if sp < 0 or sp >= len(b_list):
        return b_list
    if (b_list[sp] == OPENCHAR) or (b_list[sp] == PROTECTEDCHAR):
        b_list[sp] = '?'
        if sp % width != 0 and sp-1 >= 0: cc_helper(b_list, sp-1, width)
        if sp not in range(0, width) and sp-width >= 0: cc_helper(b_list, sp-width, width)
        if sp % width != width-1 and sp+1 < len(b_list): cc_helper(b_list, sp+1, width)
        if sp not in range(len(b_list)-width, len(b_list)) and sp+width < len(b_list): cc_helper(b_list, sp+width, width)
    return b_list

def check_connectivity (board, x, num, height, width):
    if x > num or board.count(OPENCHAR) == 0: return True
    count, start_pos = 0,0
    while start_pos < len(board) and board[start_pos] == BLOCKCHAR: start_pos += 1

    board_list = list(board)
    temp_board = ''.join(cc_helper(board_list, start_pos, width))
    count = len([x for x in range(len(temp_board)) if temp_board[x] == '?'])
    count2 = board.count(OPENCHAR) + board.count(PROTECTEDCHAR)
    return count == count2


# def add_blocks(xword, block_count, height, width):
def make_pos_list(board, height, width):
    pos_list = [i for i in range(len(board)) if board[i]=='-']
    # print(pos_list)
    return pos_list

def make_palindrome(board, num, height, width):
    n = len(board) - 1
    b_list = list(board)
    for x in range(0, len(board)//2):
        if board[x] != board[n-x]:
            if BLOCKCHAR in {board[x], board[n-x]} and OPENCHAR in {board[x], board[n-x]}:
                b_list[x], b_list[n-x] = BLOCKCHAR, BLOCKCHAR
            elif PROTECTEDCHAR in {board[x], board[n-x]} and OPENCHAR in {board[x], board[n-x]}:
                b_list[x], b_list[n-x] = PROTECTEDCHAR, PROTECTEDCHAR
            elif BLOCKCHAR in {board[x], board[n-x]} and PROTECTEDCHAR in {board[x], board[n-x]}:
                return board, len(board)
    board = ''.join(b_list)
    return board, board.count(BLOCKCHAR)

    
def block_helper(board, num, height, width): #add NUM??

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
    # new_board = make_palindrome(new_board, 0, height, width)
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

def make_word_list(text_file):
    word_list = {}
    f = open(text_file, "r")
    for w in f.readlines():
        length = len(w)
        if w in word_list:
            temp = word_list[length]
            word_list[length] = temp.append(w)

        else:
            word_list[length] = [w]

    print(word_list)

    

def main():
    inputTest = [r'^.+txt$',r'^(\d+)x(\d+)$', r'^\d+$', r'^(H|V)(\d+)x(\d+)([a-zA-Z#]+)$']
    # inputTest = r"(?<=')[^']+(?=')"
    height, width, block_count, dict_seen = 4,4,0, False
    input_words = []
    for arg in args:
        # if os.path.isfile(arg):
        #     dict_lines = open(arg, 'r').read().splitlines()
        #     dict_seen = True
        #     continue
        # print(arg)
        for test_num, retest in enumerate(inputTest):
            # print(retest)
            match = re.search(retest, arg, re.I)
            # print(test_num)
            if not match: continue
            elif test_num == 0:
                text_file = match.group(0)[1:] #help.
                # print("hi", text_file)
            elif test_num == 1:
                height, width = int(match.group(1)), int(match.group(2))
                # print(height, width)
                # print(height, width)
            
            elif test_num == 2:
                block_count = int(arg)
                # print(block_count)
            else:
                vpos, hpos, word = int(match.group(2)), int(match.group(3)), match.group(4).upper()
                input_words.append([arg[0].upper(), vpos, hpos, word])

    
    # if not dict_seen: exit("Input args are not valid")
    size = height * width
    board = OPENCHAR * size
    if block_count == size:
        board = BLOCKCHAR * size
    else:
        board = initialize(input_words, height, width)
        display(board, height, width)
        board = add_blocked_squares(board, block_count, height, width)

        # board = clean_protected(board)
        # print (block_count, board.count(BLOCKCHAR))
    # print (board)
    # print('hi')
    for word in input_words:
        direction, r, c, w = word
        w = w.upper()
        if direction.lower() == 'h':
            start = r*width + c
            board = board[:start] + w + board[start+len(w):]
        else:
            xword_list = list(board)
            for i in range(len(w)):
                xword_list[(r+i)*width + c] = w[i]
            board = ''.join(xword_list)
    board = board.replace(PROTECTEDCHAR, OPENCHAR)
    display(board, height, width)

# if __name__ == '__main___':
#     main()

main()
#Jessica Ye, 5, 2023