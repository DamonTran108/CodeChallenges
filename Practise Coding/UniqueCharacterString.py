class UniqueCharString:
    hashTable = {}

    def firstUniqueChar(self,hashTable):


        string = "hello world"
        IndexStore = 0
        letter = ""


        for i in range (len(string)):
            for character in hashTable:

                if string[i].isalpha():
                    if string[i] is character and hashTable[character] == 1:
                        ## This is a unique character--- store the index by which it appeared
                        indexStore = i
                        letter = character

                        print(letter + " is the first  unique character")
                        break
                break



    def addToHash(self,hashTable):
        #hashTable = {}
        count = 0
        string = "hello world"


        for character in string:
            #print(character)
            if character not in hashTable:
                #print ("this character aint in the string " + character)
                count = 1
                #hashTable[character] = count
                hashTable[character] = count
                continue
            else:
               #print ("this character is in the string " + character)
               hashTable[character] += 1
               hashTable.update()
               continue
        print(hashTable)

if __name__ == '__main__':
    hashTable = {}
    string = "hello world"
    my_testReverStr = UniqueCharString()
    my_testReverStr.addToHash(hashTable)
    my_testReverStr.firstUniqueChar(hashTable)



