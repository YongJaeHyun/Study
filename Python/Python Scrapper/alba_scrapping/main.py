from alba import get_jobs
from save import save_to_file

alba_jobs = get_jobs()
save_to_file(alba_jobs)