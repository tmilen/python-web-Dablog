import datetime
from flask import Flask,render_template, request
from pymongo import MongoClient
def create_app():
    app =Flask(__name__)
    client=MongoClient("mongodb+srv://tmilen:MilEn156@microblog-application.pkfhd.mongodb.net/")
    app.db=client.microblog


    @app.route("/",methods=['GET',"POST"])
    def home(): #end_point

        if request.method == "POST": # if the action is submitting the form
            entry_content=request.form.get("content")
            formatted_date=datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert_one({"content":entry_content,"date":formatted_date}) # add to the database

        entries_with_date=[
            (entry["content"],entry["date"],datetime.datetime.strptime(entry["date"],"%Y-%m-%d").strftime("%b %d"))
        for entry in app.db.entries.find({})] #suppose for display 

        return render_template("home.html",entries=entries_with_date)

    return app

