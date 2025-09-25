import os
import random
import subprocess
from datetime import datetime, timedelta

PATH = r""
START_YEAR = 2022
END_YEAR = 2025
MIN_COMMITS_PER_DAY = 0
MAX_COMMITS_PER_DAY = 3
SKIP_CHANCE = 0.3 


def generate_commit_dates(start_year, end_year):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = (end_date - start_date).days

    for i in range(delta + 1):
        yield start_date + timedelta(days=i)


def make_commits(repo, commit_date, commits_num):
    for i in range(commits_num):
        with open(os.path.join(repo, "log.txt"), "a") as f:
            f.write(f"{commit_date} - commit {i}\n")

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_COMMITTER_DATE"] = commit_date.strftime("%Y-%m-%dT%H:%M:%S")

        subprocess.run(["git", "add", "log.txt"], cwd=repo, env=env)
        subprocess.run(
            ["git", "commit", "-m", f"Commit em {commit_date.date()} #{i+1}"],
            cwd=repo,
            env=env,
        )


def main():
    os.chdir(PATH)
    for day in generate_commit_dates(START_YEAR, END_YEAR):
        if random.random() < SKIP_CHANCE:
            continue 

        commits_today = random.randint(MIN_COMMITS_PER_DAY, MAX_COMMITS_PER_DAY)
        make_commits(PATH, day, commits_today)


    subprocess.run(["git", "push", "origin", "main"], cwd=PATH)


if __name__ == "__main__":
    main()