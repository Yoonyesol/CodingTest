import sys
input=sys.stdin.readline
n = int(input())
cpu = {"ADD": "0000", "SUB": "0001", "MOV":"0010",
       "AND":"0011", "OR":"0100", "NOT":"0101", "MULT":"0110",
       "LSFTL":"0111", "LSFTR":"1000", "ASFTR":"1001",
       "RL":"1010", "RR":"1011"
       }
for _ in range(n):
    bit4 = 0
    a = list(input().split())
    if a[0][-1] == "C":
        print(cpu[a[0][:-1]], end="")
        print("1", end="")
        bit4 = 1    #비트4가 1
    else:
        print(cpu[a[0]], end="")
        print("0", end="")
    print("0", end="")  #비트5, 항상 0
    print(bin(int(a[1]))[2:].zfill(3), end="") #비트6~8, rD
    print(bin(int(a[2]))[2:].zfill(3), end="") #비트9~11, rA
    if bit4 == 0:   #rB, 12~14, 비트15=0
        print(bin(int(a[3]))[2:].zfill(3), end="")
        print("0")
    else:   ##C, 12~15
        print(bin(int(a[3]))[2:].zfill(4))

