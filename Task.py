s = "python is programming language"
f=s.split()
for words in f:
    if len(words)%2==0:
        print(words  ,"  even")
    else:
        print(words  ,"  odd")