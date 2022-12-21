from commands.run_tracked import is_running
from util import load_jobs, save_jobs, Job


def add_job(name, path):
    jobs = load_jobs()
    if len(name) > 16:
        print('name should be a max length of 16')
        return
    if not name.replace('_', 'a').isalnum():
        print('name has to be alphanumeric or underscore')
        return
    if name in jobs:
        print('job with same name already exists')
        return
    jobs[name] = Job(path, True)
    save_jobs(jobs)


def del_job(name):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return
    if is_running(name):
        print('job is running, stop this job first')
        return
    jobs.pop(name)
    save_jobs(jobs)