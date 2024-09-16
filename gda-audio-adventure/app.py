from flask import Flask, render_template, jsonify
import filetype
import os
import random

## Constants ##

AUDIO_DIR = 'static/audio'

## Variables ##

app = Flask(__name__)

## Helper Functions ##

def check_audio_files(directory):
    # Iterate over files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Guess the file type
        kind = filetype.guess(file_path)
        
        # Check if the file is an audio file
        if kind is None or not kind.mime.startswith('audio'):
            print(f"Warning: '{filename}' is not an audio file. Detected type: {kind.mime if kind else 'Unknown'}")

## Routes ##

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-audio')
def random_audio():
    # if any files are stored in audio that are not actually audio files, this will error. 
    # i think it is better to allow this to error than add some sort of catch.
    audio_files = [f for f in os.listdir(AUDIO_DIR)]
    chosen_file = random.choice(audio_files)
    return jsonify({'file': chosen_file})

## Run ##

if __name__ == '__main__':
    # warn user if a non-audio file is stored here
    check_audio_files(AUDIO_DIR)
    app.run(debug=True)