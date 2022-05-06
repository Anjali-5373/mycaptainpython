file=input("Enter file name to get it's extension")
f=file.split(".")
if (f[-1]=='py'):
    print("python")
elif(f[-1]=='doc'):
    print("word")   
elif(f[-1]=='ppt'):
    print("powerpoint")   
elif(f[-1]=='txt'):
    print("text")   
elif(f[-1]=='exe'):
    print("excel")   
elif(f[-1]=='html'):
    print("html")   
elif(f[-1]=='java'):
    print("java")   
else :
    print(f[-1])   
