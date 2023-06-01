def numSimilarGroups(strs: list[str]) -> int:
    n = len(strs)
    m = len(strs[0])
    a = []
    for i in range(n):
        t = 0
        f = 1
        for j in range(len(a)):
            if i in a[j]:
                f = 0
                t = j
                break
        if f:
            a.append({i})
            t = -1
        for j in range(i + 1, n):
            p = -1
            q = -1
            f = 1
            for k in range(m):
                if strs[i][k] != strs[j][k]:
                    if p < 0:
                        p = k
                        continue
                    if q > 0:
                        f = 0
                        break
                    if strs[i][k] != strs[j][p] or strs[i][p] != strs[j][k]:
                        f = 0
                        break
                    else:
                        q = k
            if f:
                a[t].add(j)
    f = 1
    while f:
        i = 0
        f = 0
        while i < len(a):
            j = i + 1
            while j < len(a):
                if i == j:
                    j += 1
                    continue
                if a[i] & a[j]:
                    f = 1
                    a[i] = a[i] | a[j]
                    del a[j]
                    continue
                j += 1
            i += 1
    return len(a)


print(numSimilarGroups(["uqtqjancqpfataqrlfmuglyyv","yalucgattqqpfmfunyrvqlajq","yatucgatlqqpfmfunyrvqlajq","yatucgatlqqpfrfunymvqlajq","qqyajmtpafulucvtgqqalnfry","clqugvltmryyqajqafqntafup","qmrglvyayaajqnfulcptqutfq","qcagqvyayarjlmfulnptqutfq","qnrgqvyayaajlmfulcptqutfq","qcagqvyauarjlmfylnptqutfq","clqugvltpryyqajqafqntafum","qmrgqvyayaajlnfulcptqutfq","rlqugvltyjpyqacqafqnfatum","uqtqjancqpfytyqrafmuglalv","clqugvjtmryyqalqafqntafup","qqyujmtpafalucvtgqqalnfry","clqugvltyrpyqajqafqnfatum","qnagqvyayarjlmfulcptqutfq","uqtqjancqpfataqryfmuglylv","yglavtqaptqfmfqjrunqlaycu","uqtqjancqpfatyqrafmuglylv","mvfqtcgfaqrauqytplqyuajnl","jlqugvltyrpyqacqafqnfatum","yatfcgatlqqpfruunymvqlajq","clqugvltpryyqajqafqnfatum"]))