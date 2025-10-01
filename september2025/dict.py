from collections import defaultdict
def findJudge(n: int, trust: list[list[int]]) -> int:
    #receive a list of lists where [a,b] a trusts b
    #return the number where they don't trust anyone

    #implement a key-value pair for incoming and outgoing
    #iterate through each num
    #check if the n exists in incoming and outgoing has none:
    #return the number
    #else return -1

    incoming = defaultdict(int)
    outgoing = defaultdict(int)
    print(incoming, outgoing)

    for src, dst in trust:
        outgoing[src] += 1
        incoming[dst] += 1
        print(incoming, outgoing)

    for person in range(1, n+1):
        if incoming[person] == n - 1 and outgoing[person] == 0:
            return person
    return -1

print(findJudge(4, [[1,3],[4,3],[2,3]]))