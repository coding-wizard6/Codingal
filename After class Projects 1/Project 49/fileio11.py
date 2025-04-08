file=open('sample.txt','r')
print(file.read())
file.close()

file=open('sample.txt','w')
file.write("Hello")
file.close()

file=open('sample.txt','a')
file.write("I am Sathvik")
file.close()