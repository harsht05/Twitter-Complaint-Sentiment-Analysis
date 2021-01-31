from flask import Flask,render_template,request


app=Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/<string:name>',methods=["GET",'POST'])
def yoo(name):
    if request.method == "POST":
        def getsentiment():
            tweet=request.form["tweet"]
            print(tweet)
            return redirect(url_for("postsentiment",tweet=tweet))
    else:
        return render_template(name+".html")

@app.route("/<topic>")
def postsentiment(tweet,topic):
    return render_template(topic+".html",tweet=tweet)



if(__name__=="__main__"):
    app.run(debug=True)



