import sys, getopt

usageexample = 'wordgen.py -i <inputword> -o <outputfile>'

def main(argv):
    inputword = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:",["inputword=","outputfile="])
    except getopt.GetoptError:
        print(usageexample)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(usageexample)
            sys.exit()
        elif opt in ("-i", "--inputword"):
         inputword = arg.lower()
        elif opt in ("-o", "--outputfile"):
         outputfile = arg
    with open(outputfile, 'w') as f:
        traverse_word(inputword, 0, f)

def traverse_word(inputword, index, outputfile):
    outputfile.write(inputword + '\n')
    while index < len(inputword):
        char = inputword[index]
        character_map = transpose_dict[char]
        for replacementchar in character_map:
            word = generate_word(inputword,replacementchar,index)
            traverse_word(word, index + 1, outputfile)
        index = index + 1

def generate_word(inputword, replacementchar, indextoreplace):
    return inputword[:indextoreplace] + replacementchar + inputword[indextoreplace + 1:]

def character_transpose_dict():
    return dict([
        ('a',['A','@']),
        ('b',['B','8']),
        ('c',['C','(']),
        ('d',['D','6']),
        ('e',['E','3']),
        ('f',['F','#']),
        ('g',['G','9']),
        ('h',['H','#']),
        ('i',['I','1','!','l','L']),
        ('j',['J']),
        ('k',['K','<']),
        ('l',['L','1','i','I']),
        ('m',['M']),
        ('n',['N']),
        ('o',['O','0']),
        ('p',['P']),
        ('q',['Q','9']),
        ('r',['R']),
        ('s',['S','5','z','Z']),
        ('t',['T','+','7']),
        ('u',['U']),
        ('v',['V','<','>']),
        ('w',['W','uu']),
        ('x',['X','%','xx','XX','xX','Xx']),
        ('y',['Y','?']),
        ('z',['Z','s','S'])
    ])

transpose_dict = character_transpose_dict()

if __name__ == "__main__":
    main(sys.argv[1:])