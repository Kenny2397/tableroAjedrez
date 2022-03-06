from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<n>')
def tableroAjedrez_8xn(n):
    return render_template('8xn.html',y=int(n))

@app.route('/')
def tableroAjedrez_8x8():
    return render_template('8x8.html')    

@app.route('/<m>/<n>')
def tableroAjedrez_mxn(m,n):
    return render_template('mxn.html',x=int(m),y=int(n))


@app.route('/<m>/<n>/<color1>')
def tableroAjedrez_mxn_color1(m, n, color1):
    return render_template('mxnxcolor1.html', x=int(m), y=int(n), color1=str(color1))


@app.route('/<m>/<n>/<color1>/<color2>')
def tableroAjedrez_mxn_color1_color2(m, n, color1,color2):
    return render_template('mxnxcolor1xcolor2.html', x=int(m), y=int(n), color1=str(color1), color2=str(color2))

if __name__ == "__main__":
    app.run(debug=True)