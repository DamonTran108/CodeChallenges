class RemoveCharFromString:
    def removeCharFromString(string):
        array = ['e', 'l']
        string = "hello"

        newString = ""

        for i in range(len(string)):
            if string[i]  in array:
                continue
            else:
                newString += string[i]

        print(newString)

if __name__ == '__main__':
    my_testReverStr = RemoveCharFromString()
    my_testReverStr.removeCharFromString()