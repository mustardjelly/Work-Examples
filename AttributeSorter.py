#################################################################
#@Author: 	Samuel Powell (samuel.powell@aderant.com)	#
#		Annemiek Powell (annemiekpowell@gmail.com)	#
#@Date: 	07/11/18					#
#################################################################

def Main():
    location = "String To Sort.txt"
    arrayOfLines = OpenFile(location)
    outArray = SortAttributes(arrayOfLines)
    SaveFile(outArray, location)

def OpenFile(location):
    try:
        file = open(location, "r")
        print("{0} opened!".format(location))
    except FileNotFoundError:
        print("File not found! \n{0}".format(e))
    except:
        print("General Failure!")
    inStr = ReadFile(file)
    
    file.close()
    return inStr

def ReadFile(inFile):
    inStr = inFile.readlines()
    return inStr

def SortAttributes(array):
    attribute = False
    name = False
    shortEnd = False
    outArray = []
    tempArray = []
    
    for line in array:
    #special flags
        #detects attributes
        if ("=" in line):
            attribute = True
        else:
            attribute = False
        #detects name fields
        if ("Name" not in line):
            name = False
        else:
            name = True
            
        #attributes are placed in a temp array for sorting
        if attribute:
            #detecting shortEndings
            if (line[-2:] == "\>"):
                shortEnd = True
                line = line[-2:]
                
            if not name:
                tempArray += [line]
            #name attributes should bubble to the top
            else:
                outArray += [line]
        else:
            #tempArray is empty
            if not tempArray:
                outArray += [line]
            else:
                if (len(tempArray) == 1):
                    outArray += [tempArray[0]]
                else:
                    tempArray.sort()
                    for attribute in tempArray:
                        outArray += [attribute]
                #append ending
                if (shortEnd):
                    tempArray[-1] = tempArray[-1] + "\>"
                tempArray = []
    return outArray

def ArrayPrinter(array):
    try:
        for line in array:
            print(line)
    except:
        print(array)

def SaveFile(array, location):
    filePath = location.split(".")
    filePath = filePath[0] + " sorted" + "." + filePath[1]
    
    outFile = open(filePath, "w+")
    for line in array:
        outFile.write(line)
        
    outFile.close()
    print("Successfully saved to {0}".format(filePath))
  
Main()
