from flask import Flask, render_template, request, jsonify
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

app = Flask(__name__)

# Initialize speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Get creation date & time
creation_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
creator_name = "Omkar Tambe"  # Your name as the creator

def speak(text):
    """Function to make the assistant speak"""
    engine.say(text)
    engine.runAndWait()

def process_command(query):
    """Process the user's voice or text command"""
    query = query.lower()

    if "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")  # 12-hour format
        return f"Sir, the time is {current_time}"
    
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        return f"Sir, today's date is {current_date}"

    elif "wikipedia" in query or "answer" in query:
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            return f"According to Wikipedia: {results}"
        except:
            return "Sorry, I couldn't find that on Wikipedia."

    elif "who created you" in query or "who made you" in query or "who produce you" in query or "who creat you" in query:
        return f"I was created by {creator_name}. He is my developer and mentor."

    elif "exit" in query or "stop" in query:
        return "Goodbye, sir! Have a great day."
    
    elif "hi" in query or "hello" in query:
            return "hi sir how can i help you"
    
    
    elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com")
            return "opening instagram"
    
    elif "open snapchat" in query:
            webbrowser.open("https://www.snapchat.com")
            return "opening snapchat"
    
    elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com")
            return "opening facebook"

    elif "open google" in query:
            webbrowser.open("https://www.google.com")
            return "opening google" 
    
    elif "open whatapp" in query:
            webbrowser.open("https://www.whatapp.com")
            return "opening whatapp"


    else:
        return "I'm not sure how to respond to that."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    """Receives text from frontend and responds"""
    data = request.get_json()
    query = data.get("query","")
    
    if query:
        response = process_command(query)
        return jsonify({"response": response})
    return jsonify({"response": "I didn't understand that."})

if __name__ == "__main__":
    print(f"Rocket AI Assistant Created on: {creation_time} by {creator_name}")  # Display creation time & creator name
    app.run(debug=True)