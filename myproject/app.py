from flask import Flask,render_template,redirect,request,url_for,flash
import sqlite3 as sql


app=Flask(__name__)

app.secret_key="123"

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/second")
def original():
    return render_template("index1.html")



@app.route("/booking",methods=["get","post"])
def book():
    name=request.form.get("name")
    age=request.form.get("age")
    contact=request.form.get("contact")
    destination=request.form.get("destination")
    seats=request.form.get("seats")
    conn=sql.connect("booking.db")
    cur=conn.cursor()
    cur.execute("insert into adduser (name,age,contact,destination,seats) values (?,?,?,?,?)", (name,age,contact,destination,seats))
    conn.commit()
    #if request.form.get("name"):
     #   return flash("registered seccessfully","success")
    return url_for('home')
    
    

@app.route("/view",methods=["get","post"])
def detail():
    conn=sql.connect("booking.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from adduser")
    data=cur.fetchall()
    return render_template("view.html",data=data)

@app.route("/payment",methods=["get","post"])
def pays():
    if request.method=="post":
        if request.form.get("success"):
            flash("success ","success meassage")
    return render_template("payments.html")

if __name__=="__main__":
    app.run(debug=True)