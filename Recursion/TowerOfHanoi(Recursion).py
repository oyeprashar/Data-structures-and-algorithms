def toh(n,src,dest,aux):
    if n == 0:
        return # do nothing 
    toh(n-1,src,aux,dest)
    print("Moving disc ", n," from ",src, " to ",dest)
    toh(n-1,aux,dest,src)
toh(4,'A','C','B')