def mp3(path):
    from gtts import gTTS
    import os

    fh=open(path+".txt")
    tts = gTTS(fh.read())
    tts.save(path+".mp3")
    os.system(path+".mp3")
    fh.close()

#mp3("C:\\Users\\User\\Desktop\\books\\e")
