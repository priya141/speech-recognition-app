from flask import Flask, render_template, request, jsonify
import os
import speech_recognition as sr
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize_speech', methods=['POST'])
def recognize_speech():
    try:
        # Get audio file from the request
        audio_file = request.files['audio']
        
        # Save the audio file
        audio_path = 'audio.wav'
        audio_file.save(audio_path)
        
        # Use SpeechRecognition to recognize speech
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        
        # Return the recognized text
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    try:
        # Get text from the request
        text = request.json['text']
        
        # Use gTTS to generate speech
        tts = gTTS(text)
        tts.save('output.mp3')
        
        # Return the path to the generated speech file
        return jsonify({'path': 'output.mp3'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
