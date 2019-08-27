import speech_recognition as sr
import re

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer()
device_id = sr.Microphone()


def listen():
    with sr.Microphone(device_index = 0, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:
        while(True):
            r.adjust_for_ambient_noise(source)
            print ("Say Something")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print ("you said: " + text)
                return parseAudio(text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

def parseAudio(text):
    try:
        if "use" in text:
            return ["use", text.split("use", 1)[1]]
        elif "go" in text:
            return ["go", text.split("go", 1)[1]]
        elif "data" in text:
            return ["data", text.split("data", 1)[1]]
        elif "weak" in text:
            return ["weak", text.split("weak", 1)[1]]
    except:
        print("Command not recognized")
