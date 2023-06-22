import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'videos'


@app.route('/video')
def video():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('video.html', files=files)

@app.route('/video_list')
def video_list():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({'files': files})

if __name__ == '__main__':
    app.run(debug=True)
