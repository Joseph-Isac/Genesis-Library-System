# book
import time
import os
try:
    
    print(os.getcwd())
    os.mkdir(os.getcwd()+"\\books\\")

    path_BOOKS=os.getcwd()+"\\books"
    print(path_BOOKS)

except:
    path_BOOKS=os.getcwd()+"\\books"
    print(path_BOOKS)

#************

def create():
    print()
    print()
    print("""┏--------------------------------┓   """)
    bname=input("   Enter the name of the book:  ")
    print("""└--------------------------------┛""")
    fh=open(os.getcwd()+"\\books\\"+bname+".txt",'w')
    fh.close()
    print()
    print("""┏----------------------------------------------------┓
        ✅✅ Book has been added ✅✅
└----------------------------------------------------┛""")
    print()
    print()

#************

def savetext():
    # reading the text and saving it
    #time.sleep(0.0)
    print()
    print()
    print("""┏-----------------------------------------------------------------------┓   """)
    name=input("    Enter the name of the book to which text is to be added:")
    print("""┗-----------------------------------------------------------------------┛""")
    print()
    try:
        path_identified=path_BOOKS+"\\"+name
        print(path_identified+".txt")
        fh=open(path_identified+".txt")
        fh.close()
    except:
        print("""┏----------------------------------------------------┓
        ❌❌ Book does not exist ❌❌
┗----------------------------------------------------┛""")
        return None

    import MAIN_PGM
    MAIN_PGM.MAIN_PGM(path_identified)




    
#****************************

def display():
    print()
    print()
    print("""┏-----------------------------------------------------------------------┓   """)
    bookname=input("    Enter name of the book you'd like to display:")
    print("""┗-----------------------------------------------------------------------┛""")
    print()
    print()
    path_identified=path_BOOKS+"\\"+bookname
    try:
        print("""
|===============================================|
|   Content of the file is:                     |
|-----------------------------------------------|""")
        fh=open(path_identified+".txt")
        print(fh.read())
        fh.close()
        print("""
|-----------------------------------------------|
|   End of the file                             |
|===============================================|""")
    except:
        print()
        print("""┏----------------------------------------------------┓
        ❌❌ Book does not exist ❌❌
┗----------------------------------------------------┛""")
        print()
        print()

#****************************
        
def audio():
    print()
    print()
    print("""┏-----------------------------------------------------------------------┓   """)
    bookname=input("    Enter name of the book you'd like to display:")
    print("""┗-----------------------------------------------------------------------┛""")
    print()
    print()
    path=path_BOOKS+"\\"+bookname
    
    try:
        import mp3
        mp3.mp3(path)
    except:
        print()
        print("""┏----------------------------------------------------┓
        ❌❌ Book does not exist ❌❌
┗----------------------------------------------------┛""")
        print()
        print()

#****************************
        
def books():
    path=os.getcwd()+"\\books"
    f_items=os.listdir(path)#list of files in the directory
    print("Sl.No.      Books")
    k=1
    for i in f_items:
        print(str(k)+"      "+f"{i}")
        k+=1
        
    
    
    
#*******MAIN PGM*********

while True:
    print("""
🔘---------------------------------------------------------------------------🔘
 ||    1. Display the existing books                                         ||
 ||    2. Create a book                                                      ||
 ||    3. Add text from an image to a book                                   ||
 ||    4. Display the content of a book                                      ||
 ||    5. Listen to the text of a book as an audio clip                      ||
 ||    6. Exit the program                                                   ||
🔘---------------------------------------------------------------------------🔘""")
    print()
    print("""┏--------------------------------┓   """)
    choice=int(input("""    Enter the choice number:  """))
    print("""└--------------------------------┛""")
    print()
    print()
    if choice==1:
        books()
    elif choice==2:
        create()
    elif choice==3:
        savetext()
    elif choice==4:
        display()
    elif choice==5:
        audio()
    elif choice==6:
        print("""
        ⭕⭕◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘⭕⭕
        ⭕⭕    Exiting the program     ⭕⭕
        ⭕⭕◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘◘⭕⭕""")
        exit()
    else:
        print("""""")