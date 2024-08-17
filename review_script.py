import os
from github import Github

# Initialize GitHub client
g = Github(os.getenv('GITHUB_TOKEN'))
repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
pr_number = int(os.getenv('GITHUB_PULL_REQUEST_NUMBER'))
pr = repo.get_pull(pr_number)

# Get the diff
files = pr.get_files()

# Process the diff
comments = []
for file in files:
    if file.changes > 0:
        comments.append(f"Changes in {file.filename}:\n{file.patch}")

# Post comments on the PR
if comments:
    pr.create_review(
        body="\n\n".join(comments),
        event="COMMENT"
    )