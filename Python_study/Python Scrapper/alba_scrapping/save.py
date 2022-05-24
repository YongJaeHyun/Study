import csv

def save_to_file(companies):
    for company in companies:
        name = company["name"]
        file = open(f"{name}.csv", mode="w")
        writer = csv.writer(file)
        writer.writerow(["place", "title", "time", "pay", "date"])
        for job in company["job"]:
            writer.writerow(list(job.values()))
    return