from commands.run_tracked import is_running
from util import load_jobs


def list_jobs():
    jobs = load_jobs()
    for name, job in jobs.items():
        print(f'{name:16} | {" ENABLED" if job.enabled else "DISABLED"} | {"STOPPED" if is_running(name) else "RUNNING"} | {job.path} {job.command}')