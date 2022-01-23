from dataclasses import Field
from flask import Flask, get_flashed_messages,render_template,redirect, url_for,request,flash
import clipboard
import json
app = Flask(__name__)
app.secret_key = 'Baap'
FILE_PATH = './data/data.json'

def getData():
    with open(FILE_PATH,'r') as f:
        data = json.load(f)

    return data

def saveData(key,value):
    data = getData()
    data[key] = value
    with open(FILE_PATH,'w') as f:
        json.dump(data,f)

@app.route('/copyToClipboard/<data>',methods=['GET','POST'])
def copyToClipboard(data=None):
    if request.method == 'GET':
        if data:
            clipboard.copy(data)
            flash('Text copied to clipboard')
        return redirect(url_for('home'))
    elif request.method == 'POST':
        key = request.form.get('Key')
        value = request.form.get('Value') 
        saveData(key,value)
        flash('Saved to file')
        return redirect(url_for('home'))


@app.route('/')
def home():
    messages = get_flashed_messages()
    return render_template('base.html',data = getData(),message=messages)


if __name__ == "__main__":
    app.run(debug=True)