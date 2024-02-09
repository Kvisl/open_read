with open('merge1.txt', 'r') as f1, open('merge2.txt', 'r') as f2, open('merge3.txt', 'r') as f3:

    text1 = f1.readlines()
    text2 = f2.readlines()
    text3 = f3.readlines()

    string1 = len(text1)
    string2 = len(text2)
    string3 = len(text3)

    files = [(f1.name, string1), (f2.name, string2), (f3.name, string3)]
    files.sort(key=lambda x: x[1])

    with open('merge.txt', 'w') as f:
        
        for file, count in files:
            with open(file, 'r') as f4:
                f.write(f'\n{file}\n{count}\n')
                f.writelines(f4.readlines())
