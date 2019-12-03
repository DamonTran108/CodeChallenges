class TestReverseString:

    def reverseString(word):

        word = input("Enter a word and i'll spell it backwards for you!")
        array = [word]
        length = len(word)

        print(length)



     
        i = length-1

        while i >= 0:
            print(word[i])
            i-=1


if __name__ == '__main__':
    my_testReverStr = TestReverseString()
    my_testReverStr.reverseString()