import itertools, time

# capture starting time of script
startTime = time.time()

# number of pips to start the train
initialTarget = 4

# manual entry of dominos
dominoes = [(4, 1), (1, 3), (1, 5), (3, 3), (5, 5), (3, 5)]

# all possible permutations of 0,1,2,3 -> number of dominos entered (0123, 0132, 0213, etc)
permutations = itertools.permutations(range(len(dominoes)))

# variables
longestTrain = []
currentTrainLength = 0
longestTrainLength = 0

# for each permutation
for eachpermutation in permutations:
    # reset variables for each iteration
    currentTarget = initialTarget
    currentTrain = []
    currentTrainLength = 0
    # look at each domino in this permutation
    for i in eachpermutation:
        a , b = dominoes[i]
        # add domino to current train if it matches current target
        if a == currentTarget:
            currentTrain.append((a, b))
            currentTarget = b
            currentTrainLength += 1
        elif b == currentTarget:
            currentTrain.append((b, a))
            currentTarget = a
            currentTrainLength += 1
        else:
            break
    # set longest train if current train exceeds longest train length and the 2 trains aren't identical
    if currentTrainLength >= longestTrainLength:
            if currentTrain != longestTrain:
                longestTrainLength = currentTrainLength
                longestTrain = currentTrain
                print (longestTrain)

# print time of script
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))