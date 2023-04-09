import speech_recognition as sr_lib

def listen_query():
    recognizer = sr_lib.Recognizer()
    with sr_lib.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            return query
        except sr_lib.UnknownValueError:
            return None
