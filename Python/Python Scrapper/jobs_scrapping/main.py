from flask import Flask, render_template, request, redirect, send_file
from scrapping_wwr import get_wwr_jobs
from scrapping_rok import get_rok_jobs
from scrapping_jk import get_jk_jobs
from exporter import save_to_file

app = Flask("superScrapper")
DB = {}


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existingJobs = DB.get(word)
        if existingJobs:
            rok_jobs = existingJobs.get("remoteOK")
            wwr_jobs = existingJobs.get("WeWorkRemotely")
            jk_jobs = existingJobs.get("JobKorea")
            jobs = rok_jobs + wwr_jobs + jk_jobs
        else:
            rok_jobs = get_rok_jobs(word)
            wwr_jobs = get_wwr_jobs(word)
            jk_jobs = get_jk_jobs(word)
            jobs = rok_jobs + wwr_jobs + jk_jobs
            DB[word] = {"remoteOK": rok_jobs,
                        "WeWorkRemotely": wwr_jobs, "JobKorea": jk_jobs}
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=word, resultsNumber=len(jobs), jobs=jobs)


@app.route("/advanced-search")
def advanced_search():
    try:
        word, website = request.args.getlist("word[]")
        if not (word and website):
            raise Exception()
        job = DB.get(word).get(website)
        if not job:
            print("찾은 직업이 없어요...😢")
            raise Exception()
        return render_template("report.html", searchingBy=word, resultsNumber=len(job), jobs=job, website=website)
    except:
        return redirect("/")


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        word = word.lower()
        jobs = DB.get(word)
        if "website" in request.args.keys():
            website = request.args.get("website")
            jobs = jobs.get(website)
            save_to_file(jobs, website)
        else:
            rok_jobs = jobs.get("remoteOK")
            wwr_jobs = jobs.get("WeWorkRemotely")
            jk_jobs = jobs.get("JobKorea")
            jobs = rok_jobs + wwr_jobs + jk_jobs
            website = "jobs"
            save_to_file(jobs, website)
        return send_file(f"{website}.csv")
    except:
        return redirect("/")


if __name__ == '__main__':
    app.run()
