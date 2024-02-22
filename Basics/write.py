f = open("D:\\QA Intern\\writedemo.txt","r")

f.write("This is demo file")
l = [1, 5, 8 ,9 ,56]
for items in l:
    f.write(str(items))


method = f.read
a = method()
print(a)
f.close()
