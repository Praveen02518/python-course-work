# pip install pyttsx3 SpeechRecognition pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Make the assistant speak"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # [0]=male, [1]=female (depends on system)
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user voice, fallback to text if mic not working"""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)  # better accuracy
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language='en-in')
            print("🗣️ You said:", command)
            return command.lower()
    except Exception as e:
        print("❌ Mic not working or PyAudio missing → fallback to typing")
        return input("⌨️ Type command: ").lower()

def run_assistant():
    """Main assistant loop"""
    speak("Hello! I'm your virtual assistant. How can I help you?")
    while True:
        command = listen()

        if "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "your name" in command:
            speak("I am your Python assistant!")

        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Okay bye bye! Have a good day")
            break

        elif command.strip() == "":
            speak("I didn't hear anything. Please try again.")

        else:
            speak("Sorry, I can't do that yet.")

# Run the assistant
run_assistant()
