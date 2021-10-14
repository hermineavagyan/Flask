from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
    return  render_template("index.html",times = 3, color = "blue")

@app.route('/play/<int:num>')
def play_in_num(num):
    return  render_template("index.html",times = num)
    
@app.route('/play/<int:num>/<string:color>')
def play_in_color(num,color):
#     set.background-color(color)
    return  render_template("index.html",times=num, color = color)

if __name__=="__main__":
    app.run(debug=True)