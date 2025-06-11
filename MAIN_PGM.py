import time
def MAIN_PGM(path_identified):
    # reading the text and saving it 

    import os

    def cwd(): # to find the desktop directory
        d_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')#desktop directory
        return d_dir
                
    def listingfolders(currentdir):
        foldernames=os.listdir(currentdir)#list of files in the directory
        folders={}
        print("""┏-----------------------------------------------------------------------┓   """)
        print("  File no.","File name",sep="  |||  ")
        k=1
        for i in foldernames:
            print("╬ ",str(k)+" "*(10-len(str(k))),i)
            folders[k]=i
            k+=1
        print("""┗-----------------------------------------------------------------------┛""")
        return folders,currentdir

    def saveimagedirfunc(folders1,currentdir1,saveimagedir,counter,choice_deskdir,choice_continue):
        time.sleep(1.0)
        ch=eval(input("""
    ╭---------------------------------------------------------------------------------------------------------------╮
    |    Enter file no. of  the folder where the imgs are stored                                                    |
    |---------------------------------------------------------------------------------------------------------------|
    |                               OR                                                                              |
    |---------------------------------------------------------------------------------------------------------------|
    |    Enter the File no(s) of the images in this file (seperated by a comma) whose text is to be extracted       |
    ╰---------------------------------------------------------------------------------------------------------------╯
        
        Enter input:"""))
        if str(type(ch))=="<class 'tuple'>": # a series of numbers are entered
            for i in ch:
                if (".png" in folders1[int(ch)]) or (".jpg" in folders1[int(ch)]) or (".jpeg" in folders1[int(ch)]): # only pictures of .jpg, .jpeg, .png is accepted
                    saveimagedir.append(currentdir1+"\\"+folders1[int(ch)])
                else:
                    print(folders1[int(ch)],'cannot be accepted as the extension format is wrong')
            choice_continue=input("Do you want to continue ? (Y/N):").upper()
            if choice_continue=="Y":
                print("""
                ========================================
                Going back to the desktop file
                ========================================""")
                choice_deskdir="Y"
                counter=1
                
        else: # a single number is entered
            if (".png" in folders1[int(ch)]) or (".jpg" in folders1[int(ch)]) or (".jpeg" in folders1[int(ch)]): # only pictures of .jpg, .jpeg, .png is accepted
                saveimagedir.append(currentdir1+"\\"+folders1[int(ch)])
                    
                choice_continue=input("Do you want to continue ? (Y/N):").upper()
                if choice_continue=="Y":
                    print("""
                ========================================
                Going back to the desktop file
                ========================================""")
                    choice_deskdir="Y"
                    counter=1
                            
            else:
                currentdir1+=("\\"+folders1[int(ch)]) #adding the updations so that each iteration we go in to a file
                if os.path.isdir(currentdir1)==False:
                    print("Error occured!!!!")
                    choice_continue=input("Do you want to continue ? (Y/N):").upper()
                    if choice_continue=="Y":
                        print("""
                ========================================
                Going back to the desktop file
                ========================================""")
                        counter=1

                else:
                    choice_continue=input("Do you want to continue ? (Y/N):").upper()
                    counter=0
        return currentdir1,choice_deskdir,choice_continue,counter

            
            
    def imagetotext():
        try:
            import imagetotext #module to save the text from the images
            imagetotext.imagetotext(saveimagedir,path_identified)

        except:
            print("Error occured!!!")


    #MAIN PGM
    choice_deskdir="Y"
    choice_continue="Y"
    currentdir1=cwd()
    print(currentdir1)
    saveimagedir=[]
    iteration=1
    error="N"
    counter=0
    while True: #finding out the paths of the images
        if choice_continue=="N": #required**
                    break
                
        if error!='Y':
            if iteration!=1:
                if counter!=1: 
                    choice_deskdir=input("Do you want to check a file in the desktop ? (Y/N):").upper()
                    counter=1
        else:
            choice_deskdir="Y"
            saveimagedir.clear()
            error="N"
        
        if choice_deskdir=="Y":
            currentdir1=cwd()
            folders1,currentdir1=listingfolders(currentdir1)
            print()
            currentdir1,choice_deskdir,choice_continue,counter=saveimagedirfunc(folders1,currentdir1,saveimagedir,counter,choice_deskdir,choice_continue)
            choice_deskdir="N"
            if iteration==1:
                iteration+=1
        else:
            try:
                folders1,currentdir1=listingfolders(currentdir1)
            except:
                print("Error occured !!!! \nBeginning from start")
                error="Y"
            else: #if there is no error in try block then only gets executed    
                print()
                currentdir1,choice_deskdir,choice_continue,counter=saveimagedirfunc(folders1,currentdir1,saveimagedir,counter,choice_deskdir,choice_continue)


    if saveimagedir!=[]:
        imagetotext()



