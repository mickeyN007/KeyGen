class KeyGen():
    def __init__(self, tmpInput):
        self._in = tmpInput

    # change security key to binary if not in binary
    def toHex(self):
        finalVal = ""
        if self._in.isdigit() == False:
            for char in self._in:
                 hexVal = str(bin(ord(char)))
                 hexVal = hexVal.replace("b", "")
                 finalVal += hexVal

            return finalVal

        else:
            return self._in

    def parityDrop(self):
        # create list of indexes
        indexes = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, \
                   10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, \
                   63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, \
                   14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

        keyList = list(KeyGen.toHex(self))

        newList = []

        for i in indexes:
            newList.append(keyList[i - 1])

        return newList

    # convert key to 48 bits
    def compressBox(self):
        # create list of indexes
        indexes = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, \
                   23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,  \
                   41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,\
                   44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

        keyList = KeyGen.parityDrop(self)

        newList = []

        for i in indexes:
            newList.append(keyList[i - 1])

        return newList

    def split(self):
        # convert list to string
        compressBoxString = ""
        for i in KeyGen.parityDrop(self):
            compressBoxString += i

        # split list into 2 equal parts
        listA = compressBoxString[0:28]
        listB = compressBoxString[28:56]

        
        print("A",listA)
        print("B",listB)
        
    #def shiftR(self):
        
        
        


# get input
inputB = input("Please input security key: ")


# instantiate key-gen class
k = KeyGen(inputB)
print(k.toHex())
print(k.parityDrop())
print(k.compressBox())
k.split()
    
             
        
