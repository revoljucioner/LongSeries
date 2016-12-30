inputf=open('input.txt','r')
outputf=open('output.txt','w')
a=inputf.read()
s=0
sbig=0
for i in a:
    if i == "1":
        s=s+1
    else:
        if s>sbig:
            sbig=s
        s=0
outputf.write(str(sbig))
inputf.close()
outputf.close()
