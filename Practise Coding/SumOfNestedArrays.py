class SumOfNestedArrays:
    my_testReverStr = SumOfNestedArrays()
    def sumNestedArrays(array):
        array = ['1','1','1',['3','4',['8'],['5']]]
        i = 0
        sum =0
        while i < len(my_testReverStr.array):
           print(array[i])
           if type(array[i]) is not int:
            sum += my_testReverStr.sumNestedArrays(array[i])
           else:
              sum += array[i]

           i+=1
        return sum


        #print(sum)

if __name__ == '__main__':
    my_testReverStr = SumOfNestedArrays()
    my_testReverStr.sumNestedArrays()
