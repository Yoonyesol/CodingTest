import sys
n = int(sys.stdin.readline())
post = sys.stdin.readline().strip()
stack = []
alpha = []
num_list = [0] * n
for i in range(n):
    num_list[i] = int(sys.stdin.readline())
for i in post:
    if i.isalpha():
        if i not in alpha:
            alpha.append(i)  #[A, B, C, ...]
        stack.append(num_list[alpha.index(i)])  #num_list[A = 0, B = 1, C = 2, ...]
    else:
        num2 = stack.pop()
        num1 = stack.pop()
        if i == "+":
            stack.append(num1 + num2)
        elif i == "-":
            stack.append(num1 - num2)
        elif i == "*":
            stack.append(num1 * num2)
        elif i == "/":
            stack.append(num1 / num2)
print("{:.2f}".format(stack[0]))