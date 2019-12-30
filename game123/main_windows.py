import question, os, msvcrt, time

kTimeout = 5
kCorrectNum = 0
kLevelUpPhase = set([2,4,6,8,10,12,14,16])
def LevelUp():
    if kCorrectNum in kLevelUpPhase:
        question.kDiffcult += 1

def OnCorrect():
    global kCorrectNum;
    kCorrectNum += 1
    LevelUp()

class timeoutExpired(Exception):
    pass

def input_with_timeout(timeout, timer = time.monotonic):
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche())
            if result[-1] == '\r':
                return ''.join(result[:-1])
        time.sleep(0.04)
    raise timeoutExpired

def main():
    while(1):
        q = question.generate()
        print(q)
        print(q[1])

        try:
            print("enter your answer:")
            answer = input_with_timeout(kTimeout)
        except timeoutExpired:
            print("time out!")
            break;
        #print("answer is %s, god mode is %d" % (answer, q[0]))
        if (int(answer) == q[0]):
            OnCorrect();
            print("right! score is %d next is :" % kCorrectNum)
        else:
            break

    print("game over! final score is %d" % kCorrectNum)

if __name__ == '__main__':
    main()
