def myFun1(*argv): 
    for arg in argv: 
        print (arg)
 
def myFun2(**kwargs): 
    for key, value in kwargs.items():
        print ("% s == % s" %(key, value))
   
print("Result of * args: ")
myFun1('Welcome', 'to', 'PythonandC')
 
print("\nResult of **kwargs")
myFun2(first ='Python', mid ='and', last ='C')