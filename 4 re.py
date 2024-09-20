def tocount(): 
    f= ("Hi I am Aayushi Priya. is is hi hi") 
     
    w=input("Enter a word to count:")  
    c=0 
    for i in f:
        if i==w:
            c+=1 
    print("The count of word",w,"in the story  is:",c) 
tocount()
