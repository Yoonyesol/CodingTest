def solution(begin, target, words):
    if target not in words:
        return 0
    word_path = []
    def dfs(index, start):
        if start == target:
            word_path.append(index)
            return
        for i in range(len(words)):
            chk = 0
            for j, k in zip(list(start), list(words[i])):
                if visited[i] == 1:
                    continue
                if j == k:
                    chk += 1
                if chk == len(start)-1:
                    visited[i] = 1
                    dfs(index+1, words[i])
                    visited[i] = 0
    visited = [0 for _ in range(len(words))]
    index = 0
    dfs(index, begin)
    return min(word_path)