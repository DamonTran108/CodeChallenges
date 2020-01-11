class RemoveAdjaPairs:
    def removeAdjaPairs(self):
        string = "aaaagykkok"
        newString = ""
        pairRemoved = False

        nextChar = ""


        for character in range(len(string)):
            print(string[character])
            nextChar = string[character] + 1
            if string[character] is nextChar:
                pairRemoved = True
            else:
                newString += string[character]


if __name__ == '__main__':
    my_testReverStr = RemoveAdjaPairs()
    my_testReverStr.removeAdjaPairs()