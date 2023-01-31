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
    seat=request.form.get("seats")
    conn=sql.connect("booking.db")
    cur=conn.cursor()
    cur.execute("insert into adduser (name,age,contact,destination,seat) values (?,?,?,?,?)", (name,age,contact,destination,seat))
    conn.commit()
    #if request.form.get("name"):
     #   return flash("registered seccessfully","success")
    return render_template("index1.html")
    
    

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
    return render_template("payment.html")

#@app.route("/update/<string:>")



@app.route("/paylogin",methods=["get","post"])
def login():
    user=request.form.get("name")
    num=request.form.get("num")
    dic={"user":user,"number":num}
    print(dic)
    return render_template("error.html")


@app.route("/update/<string:id>",methods=["get","post"])
def updation(id):
    
    if request.form.get("name")!=None:
       name=request.form.get("name")
       age=request.form.get("age")
       contact=request.form.get("contact")
       destination=request.form.get("destination")
       seat=request.form.get("seats")
       conn=sql.connect("booking.db")
       cur=conn.cursor()
       cur.execute("update adduser set name=?,age=?,contact=?,destination=?,seat=? where id=?",(name,age,contact,destination,seat,id))
       conn.commit()
       return redirect(url_for('home'))
    conn=sql.connect("booking.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from adduser where id=?",(id,))
    data1=cur.fetchone()
    conn.commit()
    return render_template("update.html",data=data1)



@app.route("/delete/<string:id>",methods=["get","post"])
def delete(id):
    conn=sql.connect("booking.db")
    cur=conn.cursor()
    cur.execute("delete from adduser where id=?",(id,))
    conn.commit()
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)