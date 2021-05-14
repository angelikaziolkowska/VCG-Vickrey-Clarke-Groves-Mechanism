import numpy as np

ITEMS = {'a': 0, 'b': 1, 'c': 2}
PLAYERS = {'p1': 0, 'p2': 1, 'p3': 2}


def testValuationsFromClass_muppetsExample():
    valuations = [[10, 15, 20],
                  [35, 41, 35]]
    print(computeAllPayments(valuations))
    valuations.append([25, 10, 55])
    print(computeAllPayments(valuations))


def clarkePayment(valuations, item, player):
    h = [0] * len(valuations[0])
    deduces = 0
    for i in valuations:
        if i != valuations[player]:
            h = np.add(h, i)
            deduces += i[ITEMS[item]]
    return max(h) - deduces


def computeAllPayments(valuations):
    payments = []
    for p in range(0, len(valuations)):
        playerPayments = []
        for i in ITEMS:
            playerPayments.append(clarkePayment(valuations, i, p))
        payments.append(playerPayments)
    return np.array(payments)


testValuationsFromClass_muppetsExample()


# CA2 Task 1

# valuations, each row is players valuations, each column is item
# --------------------a--b---c
valuationsPerItem = [[7, 11, 5],
                     [10, 5, 12],
                     [13, 12, 4]]

alternatives = {'a1': [[1, 1, 1],
                       [0, 0, 0],
                       [0, 0, 0]],
                'a2': [[0, 0, 0],
                       [1, 1, 1],
                       [0, 0, 0]],
                'a3': [[0, 0, 0],
                       [0, 0, 0],
                       [1, 1, 1]],
                'a4': [[1, 1, 0],
                       [0, 0, 1],
                       [0, 0, 0]],
                'a5': [[1, 1, 0],
                       [0, 0, 0],
                       [0, 0, 1]],
                'a6': [[0, 0, 1],
                       [1, 1, 0],
                       [0, 0, 0]],
                'a7': [[0, 0, 0],
                       [1, 1, 0],
                       [0, 0, 1]],
                'a8': [[0, 0, 1],
                       [0, 0, 0],
                       [1, 1, 0]],
                'a9': [[0, 0, 0],
                       [0, 0, 1],
                       [1, 1, 0]],
                'a10': [[1, 0, 1],
                        [0, 1, 0],
                        [0, 0, 0]],
                'a11': [[1, 0, 1],
                        [0, 0, 0],
                        [0, 1, 0]],
                'a12': [[0, 1, 0],
                        [1, 0, 1],
                        [0, 0, 0]],
                'a13': [[0, 0, 0],
                        [1, 0, 1],
                        [0, 1, 0]],
                'a14': [[0, 1, 0],
                        [0, 0, 0],
                        [1, 0, 1]],
                'a15': [[0, 0, 0],
                        [0, 1, 0],
                        [1, 0, 1]],
                'a16': [[0, 1, 1],
                        [1, 0, 0],
                        [0, 0, 0]],
                'a17': [[0, 1, 1],
                        [0, 0, 0],
                        [1, 0, 0]],
                'a18': [[1, 0, 0],
                        [0, 1, 1],
                        [0, 0, 0]],
                'a19': [[0, 0, 0],
                        [0, 1, 1],
                        [1, 0, 0]],
                'a20': [[1, 0, 0],
                        [0, 0, 0],
                        [0, 1, 1]],
                'a21': [[0, 0, 0],
                        [1, 0, 0],
                        [0, 1, 1]],
                'a22': [[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]],
                'a23': [[1, 0, 0],
                        [0, 0, 1],
                        [0, 1, 0]],
                'a24': [[0, 1, 0],
                        [1, 0, 0],
                        [0, 0, 1]],
                'a25': [[0, 1, 0],
                        [0, 0, 1],
                        [1, 0, 0]],
                'a26': [[0, 0, 1],
                        [1, 0, 0],
                        [0, 1, 0]],
                'a27': [[0, 0, 1],
                        [0, 1, 0],
                        [1, 0, 0]]}


def calculateVal(valuationsPerItem, set):
    # per player
    allAsBs = []
    for p, iter in zip(set, range(3)):
        pVals = []
        # player i
        for j in range(3):
            if p[j] > 0:
                pVals.append(valuationsPerItem[iter][j])
        A = np.sum(pVals) if len(pVals) > 0 else 0
        B = np.max(pVals) if len(pVals) > 0 else 0
        allAsBs.append(dict({'player': iter,
                             '(a)': A,
                             '(b)': B}))
    return allAsBs


allSetValuationsAsBs = []
# for each alternative get valuations of each player
for set in alternatives.values():
    allSetValuationsAsBs.append(calculateVal(valuationsPerItem, set))

v1_plus_v2_plus_v3 = []
for i in range(0, 27):
    a = 0
    b = 0
    print('vi(a%d) =' % (i + 1))
    for j in allSetValuationsAsBs[i]:
        print(j)
        a += j['(a)']
        b += j['(b)']
    v1_plus_v2_plus_v3.append([a, b])
print('---------------------')
print('v1 + v2 + v3 per outcome:')
v1_plus_v2_plus_v3 = np.array(v1_plus_v2_plus_v3)
for iter, i in zip(range(1, 28), v1_plus_v2_plus_v3):
    print('v1(a%d) + v2(a%d) + v3(a%d) = (a): %d, (b): %d' % (iter, iter, iter, i[0], i[1]))

print('---------------------')
print('max (a) outcome is a%d with value %d' % (np.argmax(v1_plus_v2_plus_v3[:, 0])+1, np.max(v1_plus_v2_plus_v3[:, 0])))
print('max (b) outcome is a%d with value %d' % (np.argmax(v1_plus_v2_plus_v3[:, 1])+1, np.max(v1_plus_v2_plus_v3[:, 1])))
print('---------------------')

# max_a = np.sum[v1_plus_v2_plus_v3[0]]
# print(max_a)

# Then run the VCG mechanism to compute the allocation and the Clarke payments


# # payments = computeAllPayments(valuations)
# # print(payments)  # TODO print nicer
#
# As, Bs = calculateSetValuationsForAllPlayers(valuationsPerItem, ['a', 'b', 'c'])
# print('(a) for each player:', As)
# print('(b) for each player:', Bs)

# AS third players valuation is highest for the set of all a, b, c then he wins the auction.
# PAYING THE SECOND HIGHEST BID.
