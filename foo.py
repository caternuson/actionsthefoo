import subprocess

print("Here's what changed:")

res = subprocess.getoutput('git diff --name_only origin/master')

print(res)
