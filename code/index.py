from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/student')
def student():
   return '''<form action="http://localhost:5000/result" method="POST">
     <p>Name <input type = "text" name = "Name" /></p>
     <p>Physics <input type = "text" name = "Physics" /></p>
     <p>Chemistry <input type = "text" name = "chemistry" /></p>
     <p>Maths <input type ="text" name = "Mathematics" /></p>
     <p><input type = "submit" value = "submit" /></p>
</form>'''

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return result

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
