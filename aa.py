from flask import Flask, request
from threading import Thread
from pyngrok import ngrok

def abc():
    ngrok.set_auth_token("2fXMlgN32DuoUGj6RTjz61921wr_TCUg1kJ8V6WnG5pnj53H")
    http_tunnel = ngrok.connect(5000,"tcp")

    # Print the public URL of the tunnel
    print("Public URL:", http_tunnel.public_url) 


abct = Thread(target=abc)
abct.start()

app = Flask(__name__)

appo = Flask("aa")

@app.route('/<path:path>', methods=['GET', 'POST','CONNECT'])
def index(path):
    
    
    # Print request information
    print(dict(request.headers))
    
    return f'{path} Request information printed to console.'


def aaq():
    app.run(port=5000,ssl_context="adhoc")

aaaq = Thread(target=aaq)
aaaq.start()

if __name__ == '__main__':
    appo.run(debug=True,port=6391,host="0.0.0.0") 
