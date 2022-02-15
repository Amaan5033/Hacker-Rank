


def taumBday(b,w,bc,wc,z):
    dict={bc:b,wc:w}
    minvalue=0
    cheap=min(bc,wc)
    costly=max(bc,wc)
    if (cheap+z)<costly:
        minvalue=(cheap*dict[cheap])+(cheap+z)*dict[costly]
    else:
        minvalue=(cheap*dict[cheap])+(costly*dict[costly])
    return minvalue


t=int(input("Enter the number of testcases: "))
for i in range(t):
    first_input=list(map(int,input("b and w: ").rstrip().split()))
    b=first_input[0]
    w=first_input[1]
    second_input=list(map(int,input("bc,wc and z: ").rstrip().split()))
    bc=second_input[0]
    wc=second_input[1]
    z=second_input[2]
    print(taumBday(b,w,bc,wc,z))