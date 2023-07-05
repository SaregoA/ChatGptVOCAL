#!/usr/bin/python3
import undetected_chromedriver as uc
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
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
    sleep(1)
    driver.find_element(By.XPATH, '//textarea').send_keys(Keys.ENTER)
def get_response(driver, num):
    answer = driver.find_elements(By.XPATH,
                                  "//div[contains(@class, 'markdown prose w-full break-words dark:prose-invert')]")
    return answer[num].text
def save_conversation(conversation):
    # save with the date and time on the file name
    with open(r'history_chat/conversation_{}.json'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")), 'w') as f:
        json.dump(conversation, f, indent=4)
def speak(text, lang):
    tts = gTTS(text=text, lang=lang, )  # language)
    tts.save("response.mp3")
    os.system("ffplay -af 'atempo=1.5' -nodisp -autoexit response.mp3")
    os.remove("response.mp3")
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
    uc_options = uc.ChromeOptions()
    uc_options.user_data_dir = str(pathlib.Path.home()) + ".config/chromium/"
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=uc_options, use_subprocess=True, headless=False)
    driver.get("https://chat.openai.com/")
    conversation = []
    num = 0
    print("Cosa desideri chiedere?")
    while True:
        question = listen()
        if question != "":
            if "Exit" in question:
                break
            send_input(driver, question)
            prev_answer = ""
            while True:
                answer = get_response(driver, num)
                if answer != "":
                    if answer == prev_answer:
                        break
                prev_answer = answer
                sleep(1)
            print(f"Bot: {answer}")
            speak(answer,'it')
            num += 1
            conversation.append({'question': question, 'answer': answer})
    save_conversation(conversation)