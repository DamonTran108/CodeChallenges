class TwoSumProblem:
    def twoSumproblem(num):
        num = 10
        sum = 0
        array=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        for i in range(1,len(array)):
            for j in range(i,len(array)+1):
                if i+j == num:
                    print(i)
                    print(j)
                    print("true")




if __name__ == '__main__':
    my_testReverStr = TwoSumProblem()
    my_testReverStr.twoSumproblem()
