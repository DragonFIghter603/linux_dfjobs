from commands.run_tracked import is_running
from util import load_jobs


def list_jobs():
    jobs = load_jobs()
    m = max([len(name) for name in jobs])
    for name, job in jobs.items():
        print(f'{name:{m}} | {" ENABLED" if job.enabled else "DISABLED"} | {"RUNNING" if is_running(name) else "STOPPED"} | {job.path} {job.command}')