import subprocess

print("Here's what changed:")

#res = subprocess.getoutput('git diff --name_only HEAD^ HEAD')
res = subprocess.getoutput('git log')

print(res)
