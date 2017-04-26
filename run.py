from flask import Flask,render_template, send_from_directory,request,redirect
import json
import os
import traceback
from script.latexUtil import LatexUtil
app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('soal.html')

@app.route('/pdf/<filename>',methods=['GET'])
def index3(filename):
    return send_from_directory('./latex/outpdf/',filename,mimetype='application/pdf')
    #return send_from_directory('./latex/outpdf/',filename,mimetype='application/pdf', as_attachment=True)

@app.route('/pdf/<filename>/attach',methods=['GET'])
def index4(filename):
    return send_from_directory('./latex/outpdf/',filename,mimetype='application/pdf', as_attachment=True)

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
        print(dictData)
        path,filename=lutl.process(dictData)
        print(path,filename)
    except Exception as e:
        traceback.print_exc()
        print(Exception)
        return "RESPONS FAILED"

    if filename=='' or path=='':
        return 'Fail Processing. Please come back again'
    else:
        #return 'success'
        print(path,filename)
        #return status.HTTP_201_CREATED
	host=request.host
	print(host)
	print("http://"+host+"/pdf/"+filename)
        return "http://"+host+"/pdf/"+filename
        #return "http://localhost/pdf/"+filename
        #return redirect("http://localhost/pdf", code=303)
        #return send_from_directory('./latex/outpdf/','1492890201444XX2937.pdf',mimetype='application/pdf')
        #return send_from_directory(path,filename,mimetype='application/pdf')

if __name__ == '__main__':
   global lutl
   lutl=LatexUtil() 
   import logging
   logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
   logging.basicConfig(format = logFormatStr, filename = "global.log", level=logging.DEBUG)
   formatter = logging.Formatter(logFormatStr,'%m-%d %H:%M:%S')
   fileHandler = logging.FileHandler("summary.log")
   fileHandler.setLevel(logging.DEBUG)
   fileHandler.setFormatter(formatter)
   streamHandler = logging.StreamHandler()
   streamHandler.setLevel(logging.DEBUG)
   streamHandler.setFormatter(formatter)
   app.logger.addHandler(fileHandler)
   app.logger.addHandler(streamHandler)
   app.logger.info("Logging is set up.")
   app.run(debug=True,host='0.0.0.0',port=80)
