import os


class Job:
    def __init__(self, path, command, enabled):
        self.path = path
        self.command = command
        self.enabled = enabled

    def __str__(self):
        return f'{self.path};,;,;{self.command};,;,;{self.enabled}'


def load_jobs():
    with open(os.getenv("HOME") + '/tools/dfjobs/jobfile.txt') as jobfile:
        jobs = {}
        for line in jobfile.readlines():
            name, path, command, enabled = line.split(';,;,;')
            jobs[name.strip()] = Job(path.strip(), command.strip(), enabled.strip() == 'True')
        return jobs


def save_jobs(jobs):
    with open(os.getenv("HOME") + '/tools/dfjobs/jobfile.txt', 'w') as jobfile:
        jobfile.writelines([name + ';,;,;' + str(job) for name, job in jobs.items()])