class FizzBuzz:
    def fizzBuzz(num):

        array = []
        num = 50
        for i   in range(1,num):

            if i % 3 == 0 and i % 5 == 0:
                print("fizzbuzz")
                continue

            if i % 3 == 0:
                print("fizz")
                continue

            if i % 5 == 0:
                print("buzz")
                continue


            print(i)





if __name__ == '__main__':
    my_testReverStr = FizzBuzz()

    my_testReverStr.fizzBuzz()