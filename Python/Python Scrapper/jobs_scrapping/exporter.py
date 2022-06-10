import csv


def save_to_file(jobs, website):
    file = open(f"{website}.csv", mode="w", encoding='utf-8-sig')
    writer = csv.writer(file)
    writer.writerow(["company", "info", "deadline", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
