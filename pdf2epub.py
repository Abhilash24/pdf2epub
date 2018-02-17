import sys
import os
import webbrowser

##Taking the first argument which is the filename.pdf
filename_ex = sys.argv[1]

##pdf2htmlEX converter
os.system("pdf2htmlEX " + filename_ex + " test.html")

##PDFJS
filename_js_test = 'hh.html'
webbrowser.open_new_tab(filename_js_test)

##using the loaded pdfJS file(downloaded)
filename_js = 'pdfjs.html'

##Calling new_compare.py with two arguments
os.system('python new_com.py test.html pdfjs.html')


##print filename_ex
