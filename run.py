from flask import Flask,render_template, send_from_directory,request,redirect
import json
import os
from script.latexUtil import LatexUtil
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('soal.html')

@app.route('/pdf/<filename>',methods=['GET'])
def index3(filename):
    return send_from_directory('./latex/outpdf/',filename,mimetype='application/pdf')

@app.route('/',methods=['POST'])
def index2():
    postdata=request.data
    try:
        dictData=byteify(json.loads(postdata))
        print(dictData)
    except Exception as e:
        return "WRONG JSON FILE"
    return 'ok'
    
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) 
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

@app.route('/submit', methods=['POST'])
def assemble():
    #return send_from_directory('./latex/outpdf/','1492890201444XX2937.pdf',mimetype='application/pdf')
    global lutl
    postdata=request.data
    try:
        dictData=byteify(json.loads(postdata))
        path,filename=lutl.process(dictData['listNum'])
    except Exception as e:
        return "RESPONS FAILED"

    if filename=='' or path=='':
        return 'Fail Processing. Please come back again'
    else:
        #return 'success'
        print(path,filename)
        #return status.HTTP_201_CREATED
        return "http://localhost/pdf/"+filename
        #return redirect("http://localhost/pdf", code=303)
        #return send_from_directory('./latex/outpdf/','1492890201444XX2937.pdf',mimetype='application/pdf')
        #return send_from_directory(path,filename,mimetype='application/pdf')

if __name__ == '__main__':
   global lutl
   lutl=LatexUtil() 
   lutl.setup()
   app.run(debug=True,host='0.0.0.0',port=80)
