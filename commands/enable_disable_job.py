from util import load_jobs, save_jobs


def enable(name):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return
    if jobs[name].enabled:
        print('job is already enabled')
    else:
        jobs[name].enabled = True
    save_jobs(jobs)


def disable(name):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return
    if jobs[name].enabled:
        jobs[name].enabled = False
    else:
        print('job is already disabled')
    save_jobs(jobs)