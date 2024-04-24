from flask import Flask, request
from threading import Thread
from pyngrok import ngrok

def abc():
    ngrok.set_auth_token("2fXMlgN32DuoUGj6RTjz61921wr_TCUg1kJ8V6WnG5pnj53H")
    http_tunnel = ngrok.connect(5000, hostname="0.0.0.0")

    # Print the public URL of the tunnel
    print("Public URL:", http_tunnel.public_url) 


abct = Thread(target=abc)
abct.start()

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST','CONNECT'])
def index(path):
    
    
    # Print request information
    print(dict(request.headers))
    
    return f'{path} Request information printed to console.'

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0") 
