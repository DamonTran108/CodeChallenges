import re
class LetterCap:
    def letterCapatalize(str):
        str = "hello world yeet"
        newstr = str.split()
        newString =""
        for words in newstr:
            newWords = words.capitalize()

            newString += " "+newWords

        print(newString)



    def splitString(str):
        array = []
        str= "no ho yo"
        word = ""
        tempWord =""
        i = 0
        while i < len(str):
            print(i)
            if str[i].isalpha():
                print(str[i] + " is a letter")
                word+=str[i]




            if str[i].isspace() or i == len(str)-1:
                print(word)
                tempWord = word
                word =""

                array.append(tempWord)
            i+=1
        print(word)
        print(array)






if __name__ == '__main__':
    my_testReverStr = LetterCap()
    my_testReverStr.letterCapatalize()
    my_testReverStr.splitString()