from flask import Flask, render_template, request, redirect, send_file
from scrapping_wwr import get_wwr_jobs
from scrapping_rok import get_rok_jobs
from scrapping_jk import get_jk_jobs
from exporter import save_to_file

app = Flask("superScrapper")
DB = {}


@app.route("/")
def home():
    return render_template("html/main.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existingJobs = DB.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_rok_jobs(word) + get_wwr_jobs(word) + get_jk_jobs(word)
            DB[word] = jobs
    else:
        return redirect("/")
    return render_template("html/report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = DB.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


if __name__ == '__main__':
    app.run()
