import os
import subprocess

from util import load_jobs


def run_tracked(name):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return
    if is_running(name):
        print('job already running')
        return
    job = jobs[name]
    pid = subprocess.Popen(f'cd {job.path}; {job.command}', shell=True)
    os.system(f'echo {pid} > ~/tools/dfjobs/jobs/{name}')
    subprocess.Popen(f'tail --pid={pid} -f /dev/null; rm ~/tools/dfjobs/jobs/{name}; echo shutdown')


def kill_job(name):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return
    if not is_running(name):
        print('job not running')
        return
    with open(f'~/tools/dfjobs/jobs/{name}') as pidfile:
        pid = int(pidfile.read().strip())
        os.kill(pid, 9)


def is_running(name):
    jobs = load_jobs()
    if name not in jobs:
        print('job does not exist')
        return False
    os.path.exists(f'~/tools/dfjobs/jobs/{name}')
