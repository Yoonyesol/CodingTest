T = 10
for test_case in range(1, T + 1):
    ans = 0
    input() #원본 암호문 길이
    code = list(input().split())    #원본 암호문
    input() #명령어의 개수
    command = list(input().split()) #명령어
    for i in range(len(command)):
        if command[i] == "I":
            x, y = int(command[i+1]), int(command[i+2])
            for j in range(y):
                s = command[i+3+j]
                code.insert(x+j, s)
        elif command[i] == "D":
            x, y = int(command[i+1]), int(command[i+2])
            code = code[:x]+code[x+y:]
        elif command[i] == "A":
            y = int(command[i+1])
            for j in range(y):
                code.append(command[i+2+j])
    print("#{} {}".format(test_case, ' '.join(code[:10])))