def length(t1, n):
    t2=t1*n
    l=len(t2)
    print("Tuple {} has length: {}", t2, l)
length(('1',(5,3)),2)

#Tuple {} length: ('1',(5,3)'1',(5,3)) 4
#note: here .format is missing


def length(t1, n):
    t2=t1*n
    l=len(t2)
    print("Tuple {} has length: {}". format(t2, l))
length(('1',(5,3)),2)

#Tuple ('1',(5,3)'1',(5,3)) has length:  4