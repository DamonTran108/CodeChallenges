import re
class LongestWord:

    def findLongestWord(sen):
        longestCounter = 0

        sen = "!!!!!!!!!!! Cute bye hi hello monkeys"
        tmpWord = ""
        longestWord = ""
        tmpCounter = 0
        invalidChar = ['!', '@', '"', '£', '/', '<', '>',
                       '$', '%', '^', '&', '*', '*', '(', '-', '=', '+'
                       ,'|']
        i = 0
        while i < len(sen):

            if sen[i].isspace() :
                tmpCounter= 0
                tmpWord = ""

            tmpWord += sen[i]
            tmpCounter += 1

            if longestCounter < tmpCounter:
                longestWord = tmpWord
                longestCounter = tmpCounter




            if sen[i].isspace() or sen[i] == any(ele in sen[i] for ele in invalidChar) :
                tmpCounter= 0
                tmpWord = ""

            i+=1

        print(longestCounter)
        print(longestWord)
        return sen


if __name__ == '__main__':
    my_testLongestW = LongestWord()
    my_testLongestW.findLongestWord()