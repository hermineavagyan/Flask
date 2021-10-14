from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", times = 8, cols =8, color1 = "white", color2 = "black")

@app.route('/<int:rows>')
def chessboard(rows):
    return render_template("index.html", times = rows, cols = 8,color1 = "white", color2 = "black")

@app.route('/<int:x>/<int:y>')
def coordinates(x,y):
    return render_template("index.html", times = x, cols = y,color1 = "white", color2 = "black")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def coordinatesColors(x,y, color1,color2):
    return render_template("index.html", times = x, cols = y, color1 = color1, color2 = color2)



if __name__ =="__main__":
    app.run(debug = True)
