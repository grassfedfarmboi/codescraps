# function to test if the answer to a step-counting puzzle is correct

basicSolved = [
  [23, 28, 33],
  [19, 18, 17],
  [15, 8, 1]
]

basicIncorrect = [
  [23, 28, 33],
  [19, 18, 17],
  [16, 8, 1]
]

def checkRow(row):
    highest = max(row)
    highest_index = row.index(highest)

    if highest_index == 1:
        print("Not in order: highest in middle")
        return False
    elif highest_index == 0:
        lowest_index = 2
    elif highest_index == 2:
        lowest_index = 0
    else:
        print("Error: highest index is {}".format(highest_index))
        return False

    # check if in order
    if not (row[lowest_index] < row[1] < row[highest_index]):
        print("Values not in order")
        return False

    # check steps
    step = highest - row[1]
    if row[1] - row[lowest_index] != step:
        print("Steps are not equal")
        return False

    return True

def evalPuzzle(puzzle):
    columns = [[], [], []]
    count = 0

    for row in puzzle:
        columns[0].insert(count, row[0])
        columns[1].insert(count, row[1])
        columns[2].insert(count, row[2])
        count += 1
        if checkRow(row) == False:
            return False

    for column in columns:
        if checkRow(column) == False:
            return False

    return True

answer = evalPuzzle(basicSolved)
print("basicSolved is {}".format(answer))

a2 = evalPuzzle(basicIncorrect)
print("basicIncorrect is {}".format(a2))
