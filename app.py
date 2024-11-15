from flask import Flask, render_template, request
import numpy as np
import soundfile as sf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', audio_array=None)

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio' not in request.files:
        return "No file part"

    file = request.files['audio']
    if file.filename == '':
        return "No selected file"

    # Simpan file audio
    filepath = f"./uploads/{file.filename}"
    file.save(filepath)

    # Proses file audio menjadi array numerik
    data, samplerate = sf.read(filepath)
    audio_array = np.array(data)

    # Kembalikan hasil ke template
    return render_template('index.html', audio_array=audio_array.tolist())

if __name__ == '__main__':
    app.run(debug=True)