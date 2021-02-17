import os

def audio_test():
    audio_mode = input("Mode select : ")
    if audio_mode == "20down":
        file = '19000khz.mp3'
        os.system('mpg321' + file)
    elif audio_mode == "24down":
        file = '17000khz.mp3'
        os.system('mpg321' + file)
    elif audio_mode == "30down":
        file = '16000khz.mp3'
        os.system('mpg321' + file)
    elif audio_mode == "40down":
        file = '15000khz.mp3'
        os.system('mpg321' + file)
    elif audio_mode == '50down':
        file = '12000khz.mp3'
        os.system('mpg321' + file)
