import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import time
import openai
import wikipedia
import pyjokes
import random
import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import requests
import pyttsx3
import imaplib
import email
from email.header import decode_header
import cv2
import speedtest
import webbrowser
import pywhatkit
from pytube import YouTube
import instaloader
import pyautogui
import psutil
import qrcode
import datetime

recognizer = sr.Recognizer()
openai.api_key = ""

def get_voice_command(recognizer, language='en-US', retries=3):
    for attempt in range(retries):
        with sr.Microphone() as source:
            try:
                print("Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(source, duration=2)
                
                print("Listening...")
                audio = recognizer.listen(source, timeout=10)
                
                print("Processing...")
                command = recognizer.recognize_google(audio).lower()
                
                print("You said:", command)
                return command

            except sr.UnknownValueError:
                print("Sorry, could not understand audio. Please try again.")
            except sr.RequestError as e:
                print(f"Could not request results; check your network connection. Error: {e}")
                return ""
            except sr.WaitTimeoutError:
                print("Listening timed out. Retrying...")

    print("Maximum retries reached. Failed to recognize command.")
    return ""

def speak(text, lang='en'):
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()

def speak_srb(text):
    tts = gTTS(text, lang='sr')  
    tts.save("output.mp3")
    os.system("mpg123 -q output.mp3")
    
def open_web_search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def shopping(command):
    print(command)
    if 'flipkart' in command:
        speak('Opening Flipkart online shopping website')
        webbrowser.open("https://www.flipkart.com/")
    elif 'amazon' in command:
        speak('Opening Amazon online shopping website')
        webbrowser.open("https://www.amazon.in/")
    else:
        speak("No results")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_address, subject, body):
    try:
        # Set your email credentials
        email_address = ''  # Replace with your email address
        password = ""  # Replace with your email password

        # Create the email message
        message = MIMEMultipart()
        message["From"] = email_address
        message["To"] = to_address
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(email_address, password)
            server.sendmail(email_address, to_address, message.as_string())

        print("Email sent successfully.")
        return True  # Indicate success

    except smtplib.SMTPException as e:
        print(f"Failed to send email. Error: {e}")
        return False  # Indicate failure




def read_emails():
    # Your email credentials
    email_address = ""
    app_password = ""  # Replace with your generated app password

    try:
        with imaplib.IMAP4_SSL("imap.gmail.com") as mail:
            mail.login(email_address, app_password)
            mail.select("inbox")

            _, data = mail.search(None, "ALL")
            email_ids = data[0].split()

            if email_ids:
                latest_email_id = email_ids[-1]
                _, msg_data = mail.fetch(latest_email_id, "(RFC822)")
                raw_email = msg_data[0][1]

                message = email.message_from_bytes(raw_email)
                subject, encoding = decode_header(message["subject"])[0]
                sender, encoding = decode_header(message["from"])[0]
                body = ""

                for part in message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8")
                        break

                email_content = f"Subject: {subject}\nFrom: {sender}\nBody:\n{body}"
                return email_content

            else:
                return "No emails found in the inbox."

    except Exception as e:
        return f"An error occurred: {str(e)}"




def open_specific_google_search_result(search_query, result_number):
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)
    speak(f"Opening search results for {search_query}")
 
    
    
    search_results = search_query.split()
    if 1 <= result_number <= len(search_results):
        result_url = search_results[result_number - 1]
        webbrowser.open(result_url)
    else:
        speak("Invalid result number. Please try again.")

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.DisambiguationError as e:
        options = e.options[:5]  # Limit the number of options to display
        options_str = ", ".join(options)
        return f"There are multiple results for {query}. Please be more specific. Options: {options_str}."
    except wikipedia.PageError as e:
        return f"No information found for {query}. Please try a different search term."
    except Exception as e:
        return f"An error occurred while processing your request: {str(e)}"


def tell_joke():
    joke = pyjokes.get_joke()
    return joke

def generate_random_number(start, end):
    number = random.randint(start, end)
    return str(number)

def send_email_command(command):
    speak("Whom would you like to send an email?")
    recipient ="eracaleksa35@gmail.com"

    speak("What should be the subject of the email?")
    subject = get_voice_command(recognizer, language='sr-RS')

    speak("What message would you like to send?")
    body = get_voice_command(recognizer, language='sr-RS')

    try:
        send_email(recipient, subject, body)
        speak("Email sent successfully.")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't send the email. Please try again.")


def run_kosovo():
    text = "Kosovo je srce Srbije, srce Srbije! Kosovo već dugo pokušavaju da nam otmu, ali im ga nećemo dati. Kosovo i Metohija je autonomna pokrajina u sastavu Republike Srbije, i na osnovu Rezolucije Saveta bezbednosti Ujedinjenih nacija 1244 od 10. juna 1999. godine, nalazi se pod privremenom civilnom i vojnom upravom Ujedinjenih nacija. Država Srbija, uprkos tome što su privremene institucije samouprave u Prištini jednostrano, protivno osnovnim principima međunarodnog prava, proglasile nezavisnost 17. februara 2008. godine, vodi mirnu, diplomatsku i pravnu borbu za očuvanje Kosova i Metohije u svom sastavu."

    # Create a thread for speak_srb function
    speak_thread = threading.Thread(target=speak_srb, args=(text,))

    # Create a thread for opening the web link
    web_thread = threading.Thread(target=webbrowser.open_new_tab, args=("https://youtu.be/50t-8B0v9CI",))

    # Start both threads
    speak_thread.start()
    web_thread.start()

    # Wait for both threads to finish
    speak_thread.join()
    web_thread.join()

def run_ip():
    try:
        # Use an external service to get the public IP address
        response = requests.get("https://api64.ipify.org?format=json")
        public_ip = response.json()["ip"]
        return public_ip
    except requests.RequestException as e:
        return f"Error: {e}"
    
conversation_history = "you are Legion, my private virtual assistant, acts as my personal assistant similar to Jarvis from Iron Man. It helps me with various tasks, provides information, and assists in day-to-day activities. Legion is designed to understand and respond to natural language commands. As we start our conversation, please keep in mind the context of Legion's role and feel free to interact with it as you would with a virtual assistant."


def chat_with_gpt(prompt):
    global conversation_history
    prompt_with_history = f"{conversation_history}\nUser: {prompt}"

    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the correct engine name
        prompt=prompt_with_history,
        max_tokens=150,
        n=1,
        stop=None
)


    # Extract the model's reply
    model_reply = response.choices[0].text.strip()

    # Update the conversation history
    conversation_history += f"\nUser: {prompt}\nAI: {model_reply}"

    return model_reply

def condition():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage+" percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    speak(f"Boss our system have {percentage} percentage Battery")
    if percentage >=75:
        speak(f"Boss we could have enough charging to continue our work")
    elif percentage >=40 and percentage <=75:
        speak(f"Boss we should connect out system to charging point to charge our battery")
    elif percentage >=15 and percentage <=30:
        speak(f"Boss we don't have enough power to work, please connect to charging")
    else:
        speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")

from requests import get
from bs4 import BeautifulSoup


def get_current_temperature():
    try:
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + IP_Address + '.json'
        geo_request = get(url)
        geo_data = geo_request.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        temperature_result = f"Current {search} is {temp}"
        speak(temperature_result)
    except Exception as e:
        print(f"Error fetching temperature: {e}")
        speak("Sorry, I couldn't retrieve the current temperature.")

def webCam():
    speak('Opening camera') 

    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('web camera', img)
        k = cv2.waitKey(50)
        if k == 27:  # ESC key
            break

    cap.release()
    cv2.destroyAllWindows()

def InternetSpeed():
    print("Wait a few seconds, checking your internet speed")  # Replace this with your speech function
    st = speedtest.Speedtest()
    dl = st.download()
    dl = dl / (1000000)  # converting bytes to megabytes
    up = st.upload()
    up = up / (1000000)
    print(dl, up)
    speak(f"You have {dl:.2f} megabytes per second downloading speed and {up:.2f} megabytes per second uploading speed")  # Replace this with your speech function

def locaiton():
    speak("Wait boss, let me check")
    try:
        IP_Address = get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        print(url)
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latidute = geo_data['latitude']
        org = geo_data['organization_name']
        print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
        speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        speak("Sorry boss, due to network issue i am not able to find where we are.")
        pass
def Instagram_Pro():
        speak("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        speak("Boss im downloading it.")
        mod = instaloader.Instaloader()
        mod.download_profile(name,profile_pic_only=True)
        speak("I am done boss, profile picture is saved in your main folder. ")

def scshot():
        speak("Boss, please tell me the name for this screenshot file")
        name =get_voice_command(recognizer, language='en-US')
        speak("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("I am done boss, the screenshot is saved in main folder.")

def news():
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=a2aea81adc1a4657a3ccfbc62428a4e2"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            speak(f"todays {seq[i]} news is: {headings[i]}")
        speak("Boss I am done, I have read most of the latest news")
        
import qrcode
import datetime

def qrCodeGenerator():
    speak("Boss, enter the text/link that you want to keep in the QR code.")
    input_text_link = input("Enter the Text/Link: ")

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )

    qr.add_data(input_text_link)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_file_name = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_QR.png"
    img.save(qr_file_name)

    speak(f"Boss, the QR code has been generated and saved as {qr_file_name}.")

       

def recommend_movie():
    movies = ["The Shawshank Redemption", "The Godfather", "Pulp Fiction", "Inception", "The Dark Knight"]
    recommended_movie = random.choice(movies)
    return f"I recommend you watch: {recommended_movie}"

def perform_action(command):
    if "open web" in command:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Opening a web browser")
    elif "search" in command:
        query = command.split("search", 1)[-1].strip()
        webbrowser.open_new_tab("https://www.google.com/search?q=" + query)
        speak("Searching for " + query)
    elif "time" in command:
        current_time = time.strftime("%I:%M %p")
        speak("The current time is " + current_time)
    elif "date" in command:
        current_date = time.strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "play music" in command:
        speak("What music would you like to play on YouTube?")
        music_query = get_voice_command()
        speak(f"Playing music on YouTube: {music_query}")
        open_web_search(f"YouTube {music_query}")
    elif "fix my mood" in command:
        speak("Playing mood-fixing music")
        webbrowser.open_new_tab("https://youtu.be/feXhdrVhZ34")
    elif "news"in command:
        news()
    elif 'gmail' in command:
        speak('opening your google gmail')
        webbrowser.open('https://mail.google.com/mail/')
    elif 'maps' in command:
        speak('opening google maps')
        webbrowser.open('https://www.google.co.in/maps/')
    elif 'news' in command:
        speak('opening google news')
        webbrowser.open('https://news.google.com/')
    elif 'calender' in command:
        speak('opening google calender')
        webbrowser.open('https://calendar.google.com/calendar/')
    elif 'photos' in command:
        speak('opening your google photos')
        webbrowser.open('https://photos.google.com/')
    elif 'documents' in command:
        speak('opening your google documents')
        webbrowser.open('https://docs.google.com/document/')
    elif "generate qr code" in command:
        qrCodeGenerator()
    elif 'spreadsheet' in command:
        speak('opening your google spreadsheet')
        webbrowser.open('https://docs.google.com/spreadsheets/')
    elif "legion" in command:
        speak("Starting a conversation with Legion. You can start talking.")
        
        # Initialize an empty conversation history
        conversation_history = "you are Legion, my private virtual assistant, acts as my personal assistant similar to Jarvis from Iron Man. It helps me with various tasks, provides information, and assists in day-to-day activities. Legion is designed to understand and respond to natural language commands. As we start our conversation, please keep in mind the context of Legion's role and feel free to interact with it as you would with a virtual assistant."

        while True:
            user_input = get_voice_command(recognizer, language='en-US')

            if "stop" in user_input:
                speak("Ending the conversation with legion.")
                break

            # Interact with ChatGPT
            prompt_with_history = f"{conversation_history}\nUser: {user_input}"
            gpt_response = chat_with_gpt(prompt_with_history)

            # Speak the GPT response
            speak(gpt_response)
            print(gpt_response)

            # Update the conversation history
            conversation_history += f"\nUser: {user_input}\nAI: {gpt_response}"

    elif "shopping" in command:
        shopping_command = command.split("shopping", 1)[-1].strip()
        shopping(shopping_command)
    elif "location" in command:
        locaiton()
    elif "tell me about kosovo" in command:
        run_kosovo()
    elif "tell me about"  in command:
        topic = command.split("tell me about", 1)[-1].strip()
        result = search_wikipedia(topic)
        speak(result)
    elif "tell me a joke" in command:
        joke = tell_joke()
        speak(joke)
    elif "instagram spy" in command:
        Instagram_Pro()
    elif "random number" in command:
        start, end = 1, 100  # You can modify the range as needed
        number = generate_random_number(start, end)
        speak(f"The random number is: {number}")
    elif "recommend a movie" in command:
        recommendation = recommend_movie()
        speak(recommendation)
    elif "send email" in command:
        send_email_command(command)
    elif "read email" in command:
        email_content = read_emails()
        print(email_content)
        speak(email_content)

    elif "ip" in command:
        public_ip_address = run_ip()
        speak(f"Your public IP address is: {public_ip_address}")

    elif "screenshot" in command:
        scshot()

    elif "get temperature" in command:
        get_current_temperature()

    elif "webcam" in command:
        webCam()
    elif "netspeed" in command:
        InternetSpeed()
    elif 'play' in command:
        speak("Boss, can you please say the name of the song?")
        song = get_voice_command(recognizer, language='en-US')  # Replace this with your voice recognition function
        if "play" in song:
            song = song.replace("play", "")
        speak(f'playing {song}')
        pywhatkit.playonyt(song)
        speak('playing')
    elif "download" in command:
        speak("Boss, please enter the YouTube video link you want to download.")
        link = input("Enter the YouTube video link: ")  # Replace this with your voice recognition function
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download()
        speak(f"Boss, downloaded {yt.title} from the link you provided into the main folder.")
    elif 'youtube' in command:
        speak('Opening your YouTube')
        webbrowser.open('https://www.youtube.com/')
    elif 'github' in command:
        ('opening your github')
        webbrowser.open('https://github.com/')
    elif 'gitlab' in command:
        speak('opening your gitlab')
        webbrowser.open('https://gitlab.com/-/profile')
    elif "condition" in command:
        condition()
    elif 'slides' in command:
        speak('opening your google slides')
        webbrowser.open('https://docs.google.com/presentation/')
    elif 'canva' in command:
        speak('opening your canva')
        webbrowser.open('https://www.canva.com/')
    elif 'prime' in command:
        speak('opening your amazon prime videos')
        webbrowser.open('https://www.primevideo.com/')
    elif 'netflix' in command:
        speak('opening Netflix videos')
        webbrowser.open('https://www.netflix.com/')

#otvaranje aplikacija#######################################################################################
    elif ('open calculator'in command) :
        speak('Opening calculator')
        os.startfile('C:\\Windows\\System32\\calc.exe')
    elif ('open notepad'in command) :
        speak('Opening notepad')
        os.startfile('c:\\Windows\\System32\\notepad.exe')
    elif ('open editor'in command) :
        speak('Opening your Visual studio code')
        os.startfile('..\\..\\Code.exe')
    elif ('open online classes'in command) :
        speak('Opening your Microsoft teams')
        webbrowser.open('https://teams.microsoft.com/')
    elif ('open spotify'in command) :
        speak('Opening spotify')
        os.startfile('..\\..\\Spotify.exe')
    elif ('open media player'in command) :
        speak('Opening VLC media player')
        os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
        #closing all#####################################################################################################
    elif ('kill calculator'in command) :
        speak("okay boss, closeing caliculator")
        os.system("taskkill /f /im calc.exe")
    elif ('kill paint'in command) :
        speak("okay boss, closeing mspaint")
        os.system("taskkill /f /im mspaint.exe")
    elif ('kill notepad'in command) :
        speak("okay boss, closeing notepad")
        os.system("taskkill /f /im notepad.exe")
    elif ('kill editor'in command) :
        speak("okay boss, closeing vs code")
        os.system("taskkill /f /im Code.exe")
    elif ('kill spotify'in command) :
        speak("okay boss, closeing spotify")
        os.system("taskkill /f /im Spotify.exe")
    elif ('kill media player'in command) :
        speak("okay boss, closeing media player")
        os.system("taskkill /f /im vlc.exe")
    else:
        speak("I'm sorry, I don't understand that command.")




if __name__ == "__main__":
    while True:
        print("Say 'start' to begin.")
        start_command = get_voice_command(recognizer, language='en-US')
        
        if "start" in start_command:
            speak("Hello! How can I assist you today?")
            
            while True:
                command = get_voice_command(recognizer, language='en-US')
                
                if "stop" in command:
                    speak("Goodbye!")
                    break

                perform_action(command)
            
            break
