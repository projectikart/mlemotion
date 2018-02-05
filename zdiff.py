import os

file=open("zdiff.txt",'w')
file.close()


os.system("git log --format='%H' -n 1 >zdiff.txt")
os.system("echo ' '>zdiff.txt")
os.system("git log --format='%H' -n 2 >zdiff.txt")

file=open("zdiff.txt",'r')
a=file.read()
a=a.split("\n")

a[0]=a[0].replace("'","")
a[1]=a[1].replace("'","")

query="git diff " + a[0]+" "+a[1]
print(query) 
os.system(query)

