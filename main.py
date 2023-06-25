from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import json
import random
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import speech_recognition as sr
from gtts import gTTS
import os
import pathlib
def send_input(driver, question):
    for char in question:
        driver.find_element(By.XPATH, '//textarea').send_keys(char)
        sleep(random.uniform(0.03, 0.1))
    sleep(3)
    driver.find_element(By.XPATH, '//textarea').send_keys(Keys.ENTER)
    sleep(15)
def get_response(driver, num):
    answer = driver.find_elements(By.XPATH,
                                  "//div[contains(@class, 'markdown prose w-full break-words dark:prose-invert light')]")
    return answer[num].text
def save_conversation(conversation):
    # save with the date and time on the file name
    with open('conversation_{}.json'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), 'w') as f:
        json.dump(conversation, f, indent=4)
def speak(text, lang):
    tts = gTTS(text=text, lang=lang)  # language)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="it")
            print("Hai detto: " + command)
            return command
        except:
            return ""

if __name__ == "__main__":
    options = Options()
    service = Service('geckodriver')
    profili = pathlib.Path.home().glob(".mozilla/firefox/*default-release*/")
    firefox_default_profile = next(profili, None)
    options.add_argument("-profile")
    options.add_argument(str(firefox_default_profile))
    print(str(firefox_default_profile))
    driver = Firefox(service=service, options=options)
    driver.get("https://chat.openai.com/")
    conversation = []
    num = 0
    while True:
        question = listen()
        if question != "":
            if "exit" in question:
                break
            send_input(driver, question)
            answer = get_response(driver, num)
            print(f"Bot: {answer}")
            speak(answer,'it')
            num += 1
            conversation.append({'question': question, 'answer': answer})
    save_conversation(conversation)