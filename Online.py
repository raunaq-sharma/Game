from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Start():
    return render_template('Welcome.html')
    
@app.route('/user_inputs',  methods=[ 'GET', 'POST'])
def inputs():
    #import pdb;pdb.set_trace()
    results = {}
    if request.method == 'POST':
        mood = request.form['input1']
        games = request.form['input2']
        from Games import output
        results = output(mood, games) ##print or return
        return render_template('output.html', methods = ['POST'])
    return render_template('User_inputs.html', results=results)
 
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
