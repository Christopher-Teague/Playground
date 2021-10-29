from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def boxes(num=3,color='dodgerblue'):
    return render_template("index.html", num=num, color=color)

@app.route('/play/<int:num>')
def more_boxes(num, color='dodgerblue'):
    return render_template("index.html", num=num, color=color)

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("index.html",num=num,color=color)

if __name__=="__main__":
    app.run(debug = True) 