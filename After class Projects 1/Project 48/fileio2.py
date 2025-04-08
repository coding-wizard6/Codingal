file1=open('sample.txt','r')
file2=open('newtext.txt','w')

for line in file1.readlines():
    if not(line.startswith('I')):
        print(line)
        file2.write(line)
    
file1.close
file2.close