import sys




##Taking the first argument which is the filename.pdf
filename_ex = sys.argv[1]

##Taking the first argument which is the filename.pdf
filename_js = sys.argv[2]


print(filename_ex)
print(filename_js)

with open(filename_ex, 'r') as fin:
    print fin.read()
