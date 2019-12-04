class ContinuousVowels:
<<<<<<< HEAD
    def contVowels(self):
        string = "zooooooom yoda soda ooom dooom luuum Truuueee doooooom moooooooom"
        vowels = ["a", "o", "e", "i", "u"]

        contVowelWordCounter = 0
        contVowelCounter = 0

        for character in range (len(string)):
            print(string[character])
            if string[character] in vowels:
                contVowelCounter += 1

                if contVowelCounter == 3:
                    print("contVowelWordCounter is : ")
                    print(contVowelWordCounter)
                    contVowelWordCounter +=1
                   # print(contVowelWordCounter)


            if string[character].isspace() or character ==  len(string)-1:
                contVowelCounter = 0


        print ("There are ")
        print (contVowelWordCounter)
        print(" with at least 3 continuous vowels")

if __name__ == '__main__':
    my_testReverStr = ContinuousVowels()
    my_testReverStr.contVowels()
=======

>>>>>>> ab77b956d89fc346675c6b0cab615c9f84791aff
