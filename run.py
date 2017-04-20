from flask import Flask,render_template, send_from_directory
import os
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('soal.html')
@app.route('/pdf')
def getpdf():
	currdir=os.getcwd()
	path=currdir+'/pdf/'
	print(path)
	return send_from_directory(path,'file.pdf',mimetype='application/pdf')

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=80)
