from flask import Flask, request

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST','CONNECT'])
def index(path):
    
    
    # Print request information
   # print(dict(request.headers))
    
    return f'{path} Request information printed to console.'

if __name__ == '__main__':
    app.run(debug=True,port=8080,ssl_context='adhoc') 
