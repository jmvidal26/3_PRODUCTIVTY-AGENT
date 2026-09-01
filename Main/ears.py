import speech_recognition as sr
import spacy

            





#===============================================#
#++++++++++---EARS_MODULE-------------++++++++++#
#===============================================#

def recogniton_voice_module(nlp):
    recognizer=sr.Recognizer()

#Use the main micro as audio#

    try:
        with sr.Microphone() as source:

            print("Waiting please...") #Debugging#

            recognizer.adjust_for_ambient_noise(source,duration=6)

            print("Talk please...")    #Debugging#

            audio=recognizer.listen(source,timeout=40,phrase_time_limit=40)

        try:

            text=recognizer.recognize_google(audio, language="es-ES")

            doc=nlp(text.lower())

            lemmas=[token.lemma_ for token in doc]

            response=" ".join(lemmas)

            print(response)

        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print({e})

    except sr.WaitTimeoutError:
        pass
    except OSError as e:
        print({e})
        
            










#===============================================#
#++++++++++---RUNNING AND DEBUGGING---++++++++++#
#===============================================#

if __name__=="__main__":
    try:
        nlp=spacy.load("es_core_news_sm")
        recogniton_voice_module(nlp)
    
    except OSError as e:
        print({e})
