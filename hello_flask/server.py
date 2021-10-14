from flask import Flask,render_template #import Flask to allow to create the app
app = Flask (__name__) #creates an instance of Flask class called "app"

@app.route('/') #the "@" decorator connects this route to the function immmediately following
def index():
    return render_template('index.html') #return the string "hello World" as a respose

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hello {name.capitalize()}!"

@app.route('/repeat/<string:word>/<int:num>')
def repeat(word,num):
    output = ''
    for i in range(num):
        output += f"<p>{word}</p>"
    return output

if __name__=="__main__":
    app.run(debug = True)
