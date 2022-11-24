import datetime
# Install speachRecognition
import speech_recognition as sr
import pyttsx3    # text to speach conversion


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
# to set the voice . 0-male and 1-female
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.Spvoice")
    # speak.Speak(audio)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Goodmorning")
    elif hour >= 12 and hour <= 18:
        speak("Goodafternoon")
    else:
        speak("goodevening")
    speak("This is Sharwan how may I help you")


def takecommand():         # it will take microphone input from the user and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        # it gives the time between the speaker saying and the result shown
        r.pause_threshold = 0.6
        # on increasing we need to increase the voice level then only the system can listen
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please")
    return query


if __name__ == '__main__':
    wishme()
    takecommand()
