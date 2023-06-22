from flask import Flask, render_template, request, Response, redirect, url_for, send_from_directory, jsonify, send_file
from time import time



import os,cv2
import sys
import checkSingleton as cs

app = Flask(__name__)

#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

dic={}

# g_frame = [[],[],[],[],[]]
# count = 0

def gen_frames(a):
    capture = cv2.VideoCapture(a)
    global dic
    dic[a]=capture
    #global g_frame
    #global count

    while True:
        ret, frame = capture.read()

        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_data = buffer.tobytes()
        #g_frame[a].append(buffer.tobytes())  
        # if len(g_frame[a]) > 200:
        #     del g_frame[a][0:100]
        #     count=98
        # print("count", count)
            

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')
        
def yolo_frames(a):
    # cap = dic[a]
    # global g_frame
    # global count

    # while True:
    #     if g_frame[a] is not None:
    #         frame_data = g_frame[a][count]
    #         if len(g_frame[a]) > count+1 :
    #             count+=1
    #         yield (b'--frame\r\n'
    #             b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')
    if dic.get(a) is None:
        print(a,"Number of Webcam is None")
    else:
        cap=dic.get(a)
        while True:
            ret, frame = cap.read()

            if not ret:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_data = buffer.tobytes()

            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')

# 기본 localhost:5000/ 페이지
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    return render_template('index.html', files=files)             # index.html의 형식대로 웹페이지를 보여줌


@app.route('/webcam/<idx>')
def webcam(idx):
    file=idx
    idx=idx[0]
    idx=int(idx)
    print(idx)
    return render_template('webcam.html', idx=idx,file=file)


@app.route('/webcam_feed/<int:idx>')
def webcam_feed(idx):
    return Response(gen_frames(idx), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/yolo_feed/<int:idx>')
def yolo_feed(idx):
    return Response(yolo_frames(idx), mimetype='multipart/x-mixed-replace; boundary=frame')


# 업로드할 영상 파일이 위치한 폴더 경로를 설정합니다.
UPLOAD_FOLDER = 'video'                         # 지정 경로 설정 현재 디렉토리에서 video폴더
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER     # 업로드 된 파일이 저장될 경로를 설정함

# 업로드된 영상 파일을 다운로드할 때 사용될 라우트를 설정합니다.
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# 영상 파일 업로드를 위한 라우트를 설정합니다.
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # 업로드된 파일을 저장합니다.
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('upload.html')

# 웹 페이지에서 업로드된 영상 파일을 표시하는 라우트를 설정합니다.
@app.route('/video')
def video():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('video.html', files=files)

@app.route('/video_list')
def video_list():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify({'files': files})

@app.route('/video_count')
def video_count():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    count = len(files)
    return jsonify({'count': count})

@app.route('/del/<filename>')
def del_file(filename):
    idx=filename[0]
    print("idx 체크! : ", idx)
    os.remove('video/'+filename)
    print(id(cs))
    cs.setTagStream(str(idx),True)
    print(cs.getTagStream(idx))

    return redirect('http://127.0.0.1:8000/')

@app.route('/video_stream')
def video_stream():
    return render_template('video_stream.html')
if __name__ == '__main__':
    app.run( port=8000, debug=True)