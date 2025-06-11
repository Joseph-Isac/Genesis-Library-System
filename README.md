# Genesis-Library-System
Genesis is designed so that its core purpose is to archive and save books.
However, it has a special feature - it can extract the text from images. The program is able to extract just the text from various images and the user is able to store the text under a book name. 
GLS is also able to display the book in two unique ways: 
  1. As normal text in readable format
  2. As an audio file which can be played anytime Genesis Library System takes into consideration the situation of visually handicapped people, and offers to read the saved books to the user, provided they have a stable internet connection, which is sure to be present in most modern homes and offices. The program also saves these audio playbacks as mp3 files which are accessible separately


The program follows the below structure based on functions:


| User program
|_ _ _
      | Modules
      |_ _ _
            | imagetotext.py
            | mp3.py
            | main_pgm.py
We also extensively used the below mentioned python modules in order to bring our program to reality:
  1. os: In order to access the books folder and the saved books within.
  2. time: To provide sufficient delay between each function in order to make it more user friendly and also to keep track of the program run time.
  3. pillow: This module was used so that the program was able to read and process images, which formed the core part of this project.
  4. pytesseract: This module works in conjunction with the previous module as it is used to extract the text from the scanned images.
  5. gTTs: For text to speech output, this module came in quite handy as it was simply and concise . The program is effortlessly able to connect to the internet and use standard AI voice to playback the text file.
     
