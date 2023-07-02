import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import openai

# OpenAI API-sleutel
openai.api_key = "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"

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()

def ask_question():
    # Code om een vraag te stellen aan de gebruiker

def get_answer(question):
    # OpenAI API aanroepen om het antwoord op de vraag te verkrijgen
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None
    )
    answer = response.choices[0].text.strip()
    return answer

def speak(text):
    tts = gTTS(text=text, lang='nl', slow=False)
    tts.save("answer.mp3")
    os.system("mpg321 answer.mp3")

# Spraakherkenning initialiseren
r = sr.Recognizer()

# Ongeloofwaardige woorduitdrukking instellen
magic_word = "Hé Ava"

while True:
    # Luisteren naar de gebruiker
    with sr.Microphone() as source:
        print("Zeg iets...")
        audio = r.listen(source)

    try:
        # Spraak omzetten in tekst
        recognized_text = r.recognize_google(audio, language='nl-NL')

        # Controleren of het magische woord is gezegd
        if magic_word in recognized_text:
            play_sound()
            question = ask_question()
            answer = get_answer(question)
            speak(answer)

    except sr.UnknownValueError:
        print("Sorry, ik kon je niet verstaan. Wil je het alsjeblieft herhalen voor mij?")
    except sr.RequestError:
        print("Er is een probleem ontstaan bij de spraakherkenning service. Probeer het later nog een keer.")
