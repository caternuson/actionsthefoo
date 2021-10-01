import subprocess

print("Here's what changed:")

res = subprocess.check_outptu(['git diff --name_only HEAD^ HEAD'])

print(res)
