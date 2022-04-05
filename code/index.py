from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['PROCESS_FOLDER'] = 'process/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_img(filename):
  iop = os.path.join(app.config['PROCESS_FOLDER'],filename)
  img = cv2.imread(iop)
  hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lb = np.array([110,50,50])
  ub = np.array([130,255,255])
  mask = cv2.imRange(hsv,lb,ub)
  eimg = cv2.bitwise_and(img,img,mask=mask) 
  isp = os.path.join(app.config['UPLOAD_FOLDER'],filename)
  cv2.imwrite(isp,eimg,[int(cv2.IMWRITE_JPEG_QUALITY),100)

def ris(ilp):
  import base64
  ims = ''
  with open(ilp,'rb') as img_f
    ims = img_f.read()
    ims = base64.b64encode(ims)
    ims64 = str(ims,'utf-8')
  return ims64

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        if 'file' not in request.files:
		flash('no file part')
		return render_template('upload.html')
	f = request.files['file']
        if f.filename == ''
		flash('no selected file')
		return render_template('upload.html')
	if f and allowed_file(f.filename)
		filename = secure_filename(f.filename)
		imp = os.path.join(app.config['PROCESS_FOLDER'],filename)
		f.save(imp)
		process_img(filename)
		irp = os.path.join(app.config['UPLOAD_FOLDER'],filename)
		ims = ris(irp)
		os.remove(imp)
		os.remove(irp)
		return render_template('show.html',img_stream=ims)
	return render_template('upload.html')


@app.route('/')
def index():
    return '''<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Serverless Devs - Powered By Serverless Devs</title>
    <link href="https://example-static.oss-cn-beijing.aliyuncs.com/web-framework/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<div class="website">
    <div class="ri-t">
        <h1>Devsapp</h1>
        <h2>这是一个 Flask 项目</h2>
        <span>自豪的通过Serverless Devs进行部署</span>
        <br/>
        <p>您也可以快速体验： <br/>
            • 下载Serverless Devs工具：npm install @serverless-devs/s<br/>
            • 初始化项目：s init start-flask<br/>

            • 项目部署：s deploy<br/>
            <br/>
            Serverless Devs 钉钉交流群：33947367
        </p>
    </div>
</div>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
