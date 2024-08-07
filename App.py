from flask import Flask,render_template,request
from TopicAdder import Get_Repos,Auto_Topic,Manual_Topic


app = Flask(__name__,template_folder="Templates")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Repos",methods=["post"])
def API():
    Data = Get_Repos(request.form.get("Key"))
    if Data == None: return "Not Found", 404
    else:return render_template("SeeRepos.html",Repos=Data,Account=request.form.get("Key"))

@app.route("/Auto/true",methods=["post"])
def AutoTopics():
   Auto_Topic(request.form.get("Key"))
   return render_template("AutoPage.html")

@app.route("/Auto?false",methods=["post"])
def ManualTopics():
    Manual_Topic()
    return "Hello World"



if __name__ == "__main__":
    app.run(debug=True)