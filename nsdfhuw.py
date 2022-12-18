import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("Hello i am Karan Mehta")

def takeCommand():
     r=sr.Recognizer()
     sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening........")
          audio=r.listen(source)
          try:
               print("Recognize.........")
               query=r.recognize_google(audio, language='en')
          except Exception as e:
               print("Try Again.......")
               return "None"
          return query
if __name__=="__main__":
     while True:
          query=takeCommand().lower()
          if 'light on' in query:
               print("Light On..........")
               speak("Light On..........")
          elif 'light off' in query:
               print("Light Off.........")
               speak("Light Off.........")
          elif 'exit' in query:
               break