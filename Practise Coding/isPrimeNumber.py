class isPrime:
    def isPrimeNumber(num):
        num = 11
        counter = 0
        for i in range(1,num+1):
            #print(i)
            if  num % i == 0:
                #print("is a prime")
                counter += 1
                print(counter)

        if counter > 2:
            print("not a prime")
        else:
            print("is a prime")



if __name__ == '__main__':
    my_testReverStr = isPrime()
    my_testReverStr.isPrimeNumber()