class testFactorial:



    def firstFactorial(num):
        total = 1
        num = int(input("Enter a number"))

        i = 1
        while i < num +1:
            print(i)

            total*= i
            i+=1
        print (total)
        return num



if __name__ == '__main__':
    my_test = testFactorial()
    my_test.firstFactorial()
