class CheckNumberOfParenthisis:
    def checkNumOfP(string):
        string = "((((()))))"
        countO = 0
        countC = 0

        for i in range(len(string)):
            if string[i] is "(":
                countO += 1

            else:
                countC += 1

        if countO == countC:
            print("valid")
            return True

        print("not valid")
        return False

if __name__ == '__main__':
    my_testReverStr = CheckNumberOfParenthisis()
    my_testReverStr.checkNumOfP()