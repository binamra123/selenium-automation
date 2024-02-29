f = open("D:\\QA Intern\\writedemo.txt","w")

f.write("This is demo file\n")
l = [1, 5, 8, 9, 56]
for item in l:
    f.write(str(item) + "\n")


f = open("D:\\QA Intern\\writedemo.txt","r")
content = f.read()
print(content)

