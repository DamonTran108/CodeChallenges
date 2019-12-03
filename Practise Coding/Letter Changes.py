class LetterChange:
    def LetterChanges(str):
        str = "fun times*3"
        alphabet = ['a','b','c','d','e','f','g','h'
                    ,'i','j','k','l','m','n',
                    'o','p','q','r','s',
                    't','u','v','w','x','y','z']

        vowels = ['a', 'o', 'e', 'i', 'u']

        newstr1 = "ifz"
        newstr = ""
        str.split(',')
        iCounter = 0


        #print(len(alphabet))

        while iCounter < len(str):
            print(str[iCounter])
            jCounter = 0



            while jCounter < len(alphabet):

                print(alphabet[jCounter])


                if str[iCounter] is alphabet[jCounter]:
                   # print(str[iCounter])
                    #print(alphabet[jCounter])
                    newstr += alphabet[jCounter+1]


                jCounter += 1

            iCounter += 1
        newerStr = ""


        cap = ""
        z = 0
        while z <len(newstr):
            if newstr[z] in vowels:

                cap = newstr[z].capitalize()

                newstr = newstr.replace(newstr[z], cap)

            z+=1



        print(newstr)







if __name__ == '__main__':
    my_testLongestW = LetterChange()
    my_testLongestW.LetterChanges()