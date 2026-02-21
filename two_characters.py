def two_characters(s):

    best=0

    chars=set(s)

    for a in chars:
        for b in chars:

            if a!=b:

                t=[c for c in s if c==a or c==b]

                valid=True

                for i in range(1,len(t)):

                    if t[i]==t[i-1]:
                        valid=False

                if valid:
                    best=max(best,len(t))

    return best
