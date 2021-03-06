#A test for creating a simple HTTP server using flask
#Parse URL Query String for further process.
# Edit 2022/2/20 2
# Edit one more


from flask import Flask
from flask import request
from urllib.parse import urlparse
from urllib.parse import parse_qs

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test",methods = ['POST','GET'])
def hello_test():
    if request.method == 'GET':
        url_str = request.url
        print(url_str)
        parse_result_obj = urlparse(url_str)
        print(parse_result_obj)
        qs_obj = parse_qs(parse_result_obj.query)
        for k,v in qs_obj.items():
            print(k)
            print(v[0])
            print('\n')
        ret_val = "<p> GET </p>"
    else:
        print(request.form['txt1'])
        print(request.form['txt2'])
        ret_val = "<p> NOT GET </p>"
        
    return ret_val

@app.route("/jsontest",methods = ['POST','GET'])
def hello_jsontest():
    content = request.get_json()
    print(content)
    return ""