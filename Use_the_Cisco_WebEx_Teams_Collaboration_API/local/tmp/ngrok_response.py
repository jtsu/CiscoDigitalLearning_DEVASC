from flask import Flask, request
 
app = Flask(__name__)
port = 5005
 
@app.route("/", methods=['GET','POST'])
def index():
    return f"Request received on local port {port}"
 
if __name__=='__main__':
    app.run(host="0.0.0.0", port=port)