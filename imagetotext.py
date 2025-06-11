def imagetotext(saveimagedir,path_identified):
    from PIL import Image
    from pytesseract import pytesseract
          
    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    for i in saveimagedir:
        
        image_path = i
        #print(image_path)
        # Opening the image & storing it in an image object
        img = Image.open(image_path)      
        # Providing the tesseract executable
        # location to pytesseract library
        pytesseract.tesseract_cmd = path_to_tesseract
        # Passing the image object to image_to_string() function
        # This function will extract the text from the image
        text = pytesseract.image_to_string(img)
        # Displaying the extracted text
        #print(text[:-1])
        #writing to text filter                 
        lines=text[:-2].split("\n")
        fh=open(path_identified+".txt","a")
        for j in lines:
            fh.write(j+"\n")
        fh.close()


        

