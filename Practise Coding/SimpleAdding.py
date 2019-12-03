class SimpleAdding:
    def simpleAdding(num):
        total = 0
        num = 12
        i = 0

        while i <= num:
            total += i
            i+=1

        print(total)

if __name__ == '__main__':
    my_testLongestW = SimpleAdding()
    my_testLongestW.simpleAdding()