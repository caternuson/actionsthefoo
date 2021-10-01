import subprocess

print("Here's what changed:")

res = subprocess.getoutput('git diff --name-only origin/main')

print(res)
