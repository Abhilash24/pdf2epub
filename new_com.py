import sys
from bs4 import BeautifulSoup
import codecs


##Taking the first argument which is the filename.pdf
filename_ex = sys.argv[1]

##Taking the first argument which is the filename.pdf
filename_js = sys.argv[2]


print(filename_ex)
print(filename_js)



# ** Load from file **
#  Load HTML from output of PDFjs
jsFile = BeautifulSoup( open ("" + filename_js), 'html5lib' )
#  Load HTML from output of pdf2htmlEX
exFile = BeautifulSoup( open ("" + filename_ex), 'html5lib' )

# Extract text from jsFile
jsText = jsFile.find('div', {'id':'viewer'}).text
# Extract text from exFile
exText = exFile.find('div', {'id':'page-container'}).text

# Size of files
print("Original")
print("Size of exText is {0}. Size of jsText is {1}".format(len(exText), len(jsText) ))

# Function to check if given unicode can be mapped to ASCII char
def isASCII(ch):
    return ch.encode('ascii','ignore') == ch.encode('ascii','replace')
    pass



# Special case character
# Unicode Character 'LATIN SMALL LIGATURE FF' (U+FB00) is used instead of two ff
# This should be changed in source code - todo***
if u'\ufb00' in exText and u'\ufb00' not in jsText:
    print("Replacing u'\ufb00' with u'ff'")
    exText = exText.replace(u'\ufb00', u'f' + u'f')
    pass


elif u'\ufb03' in exText and u'\ufb03' not in jsText:
    print("Replacing u'\ufb03' with u'ffi'")
    exText = exText.replace(u'\ufb03', u'f' + u'f' + u'i')
    pass

elif u'\ufb04' in exText and u'\ufb04' not in jsText:
    print("Replacing u'\ufb04' with u'ffl'")
    exText = exText.replace(u'\ufb04', u'f' + u'f' + u'l')
    pass

elif u'\ufb01' in exText and u'\ufb01' not in jsText:
    print("Replacing u'\ufb01' with u'fi'")
    exText = exText.replace(u'\ufb01', u'f' + u'i')
    pass

elif u'\ufb02' in exText and u'\ufb02' not in jsText:
    print("Replacing u'\ufb02' with u'fl'")
    exText = exText.replace(u'\ufb02', u'f' + u'l')
    pass

elif u'\ufb06' in exText and u'\ufb06' not in jsText:
    print("Replacing u'\ufb06' with u'st'")
    exText = exText.replace(u'\ufb06', u's' + u't')
    pass


elif u'\ufb05' in exText and u'\ufb05' not in jsText:
    print("Replacing u'\ufb05' with u'ft'")
    exText = exText.replace(u'\ufb05', u'f' + u't')
    pass


#Making mapping for each character in _ex file
 
qbfile = open("" + filename_ex,"r")
b = qbfile.read()
#print b

qbfile.close()

count = 0
#mapping for each characters in the _ex file
mappings = {}

#for loop for mapping each of the character in _ex file to an integer
for letter in b:
    mappings[count] = b[count]
    count = count + 1  


print mappings[1] + "&&&"


# ** Preprocess the text **
# Remove spaces: There is a mismatch between whitespaces in both files
exText = "".join(exText.split())
jsText = "".join(jsText.split())

def method1(list,search_name):
     for num,name in list.iteritems():
             if name == search_name:
                   return num
  

# Size of files
print("Pre Processed")
print("Size of exText is {0}. Size of jsText is {1}".format(len(exText), len(jsText) ))

# ** Compare the files **
print("The following are valid changes")
for exChar, jsChar in zip(exText,jsText):
    # Detect difference
    if exChar != jsChar:
        # To check for anomility. Expected behaviour: jsChar should be Unicode and exChar should be Ascii mismatch
        if (isASCII(exChar) and isASCII(jsChar)) :
            print(exChar + " " + jsChar + ' Check')
        else:
            print(exChar + " " + jsChar + method1(mappings, exChar) )  #Trying to print the position of the character exChar here.
               #print mappings.keys()[mappings.values().index(exChar)]
                  
                # for num, char in mappings.iteritems():    
                 # if (char == exChar):
                   ##b[num] = jsChar
                  # print num
                 
        pass
pass
