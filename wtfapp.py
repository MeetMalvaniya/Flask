from flask import Flask,render_template,request,flash
from wtfform import contactform

app=Flask(__name__)
app.secret_key="development key"

@app.route("/contact",methods=["GET","POST"])
def contact():
    form=contactform()
    if request.method=="POST":
        if form.validate()==False:
            flash("All field required")
            return render_template("contact.html",form=form)
        else:
            return render_template("success.html")
    if request.method == "GET":
        return render_template("contact.html",form=form)
    
if __name__=="__main__":
    app.run(debug=True)