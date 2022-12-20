from util import load_jobs, save_jobs, Job


def add_job(name, path):
    jobs = load_jobs()
    if len(name) > 16:
        print('name should be a max length of 16')
    if name in jobs:
        print('job with same name already exists')
        return
    jobs[name] = Job(path, True)
    save_jobs(jobs)