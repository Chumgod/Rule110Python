def cycle(startLine, iterations):
    accumulator = [0, 0, 0]  # 3 bits
    lineNum = 0  # 1 bit
    colNum = 0  # technically 4 bits since this goes to 16
    subLine = [0] * len(startLine)
    lines = [startLine, subLine]  # 2 arrays of 16 bits each

    def mcolnum(symb, num):
        if symb == "+":
            if num == len(lines[1]) - 1:
                num = 0
                return num
            else:
                num += 1
                return num
        else:
            if num == 0:
                num = len(lines[1]) - 1
                return num
            else:
                num -= 1
                return num

    def rule(threeBits):
        if threeBits == [0, 0, 0]:
            return 0
        elif threeBits == [0, 0, 1]:
            return 1
        elif threeBits == [0, 1, 0]:
            return 1
        elif threeBits == [0, 1, 1]:
            return 1
        elif threeBits == [1, 0, 0]:
            return 0
        elif threeBits == [1, 0, 1]:
            return 1
        elif threeBits == [1, 1, 0]:
            return 1
        elif threeBits == [1, 1, 1]:
            return 0

    print(lines[lineNum])
    for y in range(0, iterations):
        for x in lines[lineNum]:
            accumulator[0] = lines[lineNum][mcolnum("-", colNum)]
            accumulator[1] = lines[lineNum][colNum]
            accumulator[2] = lines[lineNum][mcolnum("+", colNum)]
            if lineNum == 0:
                lines[1][colNum] = rule(accumulator)

            else:
                lines[0][colNum] = rule(accumulator)

            accumulator = [0, 0, 0]
            colNum += 1
        colNum = 0
        if lineNum == 0:
            lineNum = 1
            print(lines[1])
        else:
            lineNum = 0
            print(lines[0])


cycle([1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], 100)
