import sys
TC = int(sys.stdin.readline())
for _ in range(TC):
    #N:문서갯수 M:순서를 알고자 하는 문서
    N, M = map(int, sys.stdin.readline().split())
    pri = list(map(int,sys.stdin.readline().split()))
    page_list = [(page, idx) for (idx, page) in enumerate(pri)]
    page_list2 = []
    if len(page_list) == 1:
        print(1)
    else:
        for i in range(N):
            while page_list:
                if page_list[i][0] >= max(page_list)[0]:
                    page_list2.append(page_list.pop(0))
                elif page_list[i][0] < max(page_list)[0]:
                    page_list.append(page_list.pop(0))
    for i in page_list2:
        if i[1] == M:
            print(page_list2.index(i)+1)