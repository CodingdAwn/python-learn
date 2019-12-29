import question, os, signal

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

class InputTimeoutError(Exception):
    pass

def interrupted(signum, frame):
    raise InputTimeoutError

def main():
    while(1):
        q = question.generate()
        print(q)
        print(q[1])

        #一定时间内不输入就算失败
        signal.signal(signal.SIGALRM, interrupted)
        signal.alarm(kTimeout)
        try:
            answer = input("enter your answer:")
        except InputTimeoutError:
            print("time out!")
            break;
        #print("answer is %s, god mode is %d" % (answer, q[0]))
        signal.alarm(0)
        if (int(answer) == q[0]):
            print("right! next is :")
            OnCorrect();
        else:
            break

    print("game over!")

if __name__ == '__main__':
    main()
