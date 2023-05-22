#Creating Basic API using Flask and REST API Methods - GET and POST
from flask import Flask, render_template, redirect, url_for ,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/score/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return(render_template('result.html',result=res))

@app.route('/fail/<int:score>')
def fail(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"

    return(render_template('result.html',result=res))

#Result Checker
@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks<30:
        result='Fail'
    else: 
        result='Pass'
    return(redirect(url_for(result,score=marks)))

@app.route('/submit',methods=["GET","POST"])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        chemistry=float(request.form['chemistry'])
        comp_science=float(request.form['computerscience'])
        total_score=(science+maths+chemistry+comp_science)/4
        res=""
        if total_score>=50:
            res="success"
        else:
            res="fail"
        return(redirect(url_for(res,score=total_score)))
if __name__=="__main__":
    app.run(debug=True)