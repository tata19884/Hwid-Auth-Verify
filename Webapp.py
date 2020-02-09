import logging, json

from flask import Flask, render_template, request

# To disable the werkzeug logger
'''log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)'''

app = Flask('')
hwidsList = []

with open ("auth/hwid.txt", "r") as f:
  hwids = f.read()
hwidsSplitted = hwids.split("\n")
for i in range(0, len(hwidsSplitted)):
  hwidsList.append(hwidsSplitted[i])

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/backend', methods=['GET'])
def test():
    hwid = request.args.get('hwid')
    
    true = {
     'whitelisted': True,
     'status': 200
    }

    false = {
     'whitelisted': False,
     'status': 401
    }

    if hwid not in hwids:
      return json.dumps(false), 401
    else:
      return json.dumps(true), 200

@app.errorhandler(404) 
def not_found(e): 
    return render_template("NotFoundError.html"), 404

if __name__ == '__main__':
    app.run(
      host="localhost", 
      port=8080,
      debug=True
    )
