from util import load_jobs, save_jobs, Job


def del_job(name, path):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return
    jobs.pop(name)
    save_jobs(jobs)