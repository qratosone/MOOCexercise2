n=input()
a=n/3600
b=n%3600/60
c=(n%3600)%60
print "%d %d %d"%(a,b,c)