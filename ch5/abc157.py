import sys
"""
学んだこと
入出力高速化
短い配列はベタ書き
readlineは改行含むから注意
"""


def main():
    input = sys.stdin.readline
    bingo = [list(map(int,input()[:-1].split())) for _ in range(3)]
    
    N = int(input())
    M = [[False,False,False], [False,False,False], [False,False,False]]
    for _ in range(N):
        b = int (input())
        for i in range(3):
            for j in range(3):
                if bingo[i][j] == b:
                    M[i][j] = True

    arch = False #達成
    
    #横
    for i in range(3):
        if M[i][0] and M[i][1] and M[i][2]:
            arch = True
    #縦
    for i in range(3):
        if M[0][i] and M[1][i] and M[2][i]:
            arch = True
    #斜め
    if M[0][0] and M[1][1] and M[2][2]:
        arch = True
    
    

    if M[0][2] and M[1][1] and M[2][0]:
        arch = True
    
    if arch:
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()