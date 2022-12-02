def rps_part1():
    res = []
    score = 0
    i = 0
    with open("input.txt", "r") as f:
        for line in f:
            if line:
                res.append(str(line).strip())
        while i < len(res):
            if res[i][0] == "A":
                if res[i][2] == "X":
                    score += 4
                elif res[i][2] == "Y":
                    score += 8
                elif res[i][2] == "Z":
                    score += 3
                i += 1
            elif res[i][0] == "B":
                if res[i][2] == "X":
                    score += 1
                elif res[i][2] == "Y":
                    score += 5
                elif res[i][2] == "Z":
                    score += 9
                i += 1
            elif res[i][0] == "C":
                if res[i][2] == "X":
                    score += 7
                elif res[i][2] == "Y":
                    score += 2
                elif res[i][2] == "Z":
                    score += 6
                i += 1 
        print(score)
rps_part1()

def rps_part2():
    res = []
    score = 0
    i = 0
    with open("input.txt", "r") as f:
        for line in f:
            if line:
                res.append(str(line).strip())
        while i < len(res):
            if res[i][0] == "A":
                if res[i][2] == "X":
                    score += 3
                elif res[i][2] == "Y":
                    score += 4
                elif res[i][2] == "Z":
                    score += 8
                i += 1
            elif res[i][0] == "B":
                if res[i][2] == "X":
                    score += 1
                elif res[i][2] == "Y":
                    score += 5
                elif res[i][2] == "Z":
                    score += 9
                i += 1
            elif res[i][0] == "C":
                if res[i][2] == "X":
                    score += 2
                elif res[i][2] == "Y":
                    score += 6
                elif res[i][2] == "Z":
                    score += 7
                i += 1 
        print(score)
rps_part2()
