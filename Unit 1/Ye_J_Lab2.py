# Jessica Ye
# Date: 9/22/21

# from Ye_J_U1_L1 import generate_children


def readTxt():
    f = open("words.txt")
    lines = f.readlines()
    f.close()

    returnlines = [w.strip() for w in lines]

    return returnlines

# print(readTxt())
possibleWords = readTxt()

def generate_adjacents(current, word_list):
    adj_list = set()
    for c in "abcdefghijklmnopqrstuvwxyz":
        for i in range(len(current)):
            # print(current[:i]+c+current[i+1:])
            if (current[:i]+c+current[i+1:] in word_list):
                adj_list.add(current[:i]+c+current[i+1:])

    return adj_list

def display_path(n, explored, start): #CHECK IF CORRECT!!
    l = []
    while explored[n] != "s":
        l.append(n)
        n = explored[n]
    l.append(start)
    # print()
    l = l[::-1]

    print(l)
    print("The number of steps:", len(l))
    return ""

def display_path1(n, explored, start, totalSteps): #CHECK IF CORRECT!!
    l = []
    while explored[n] != "s":
        l.append(n)
        n = explored[n]
    l.append(start)
    # print()
    l = l[::-1]
    # print("Path:", end=" ")
    print(l)
    # print("The number of steps:", len(l), totalSteps)
    # print("Steps within", totalSteps, "limit:", len(l))
    # return (l, len(l))
    length = str(len(l))

    return ("Steps within "+ str(totalSteps) + " limit: "+length )


def BFS(start, end, word_dict):
    explored = {start:"s"}
    Q = [start]

    if len(Q)==0:
        return()
    while len(Q)!=0:
        s = Q.pop(0)
        if (s == end):
            return (display_path(s, explored, start))
        for a in generate_adjacents(s, word_dict):
            if a not in explored:
                Q.append(a)
                explored[a]=s

    return (["No solution"], 0)


def recur(start, end, word_dict, explored, limit, orig):
    # cutoff;
    if start == end: 
        # print ("something")
        return(display_path1(start, explored, list(explored.keys())[0], orig))
    # elif limit == 0: return ""#"cutoff"
    elif not limit == 0:
        #cutoff = False
        # print(limit, generate_adjacents(start, word_dict))
        for a in generate_adjacents(start, word_dict):
            if a not in explored:
                explored[a]=start
                result = recur(a, end, word_dict, explored, limit-1, orig)
                del explored[a]
                if result == "No Solution": cutoff = True
                elif result != "No Solution": return result
        #if cutoff:
            #return cutoff
            
    return "No Solution"

def DLS (start, end, word_dict, limit):
    explored = {start:"s"}
    # Q = [start]

    # if len(Q)==0:
    #     return ()
    # while len(Q)!=0:
    #     s = Q.pop()
    #     if (s==end):
    #         return(display_path(s, explored, start))
    #     for a in generate_adjacents(s):
    #         if a not in explored and limit!=0:
    #             recur(start, end, word_dict, explored, limit-1) #recur???
    # return ("No solution")


    return recur(start, end, word_dict, explored, limit-1, limit)


def IDS (start, end, word_dict):
    # depth = 1
    for i in range(1,21):
        result = DLS(start, end, word_dict, i)
        if result != "No Solution":
            return ("Steps: "+ result.split()[2])
    else:
        return "No Solution"

        # else:
        #     depth = depth+1

def main():
    startWord1 = input("Type the starting word: ").strip()
    goalWord1 = input("Type the goal word: ").strip()


    print(BFS(startWord1, goalWord1, possibleWords))

    limitSteps = int(input("Type the limit (1 - 20): ").strip())
    startWord2 = input("Type the starting word: ").strip()
    goalWord2 = input("Type the goal word: ").strip()
    print("Path:", end=" ")
    print(DLS(startWord2, goalWord2, possibleWords, limitSteps))
    print("Shortest Path:", end=" ")
    print(IDS (startWord2, goalWord2, possibleWords) )

if __name__ == '__main__':
    main()