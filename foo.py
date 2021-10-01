import subprocess

all_changes = subprocess.getoutput('git diff --name-only origin/main').split('\n')

print("Here's what changed:")
print(all_changes)

changes_to_test = []
print("Looking for subfolders...")
for path in all_changes:
    if path.startswith('.') or not "/" in path:
        print("  ignoring: ", path)
        continue
    print("  found: ", path)
    changes_to_test.append(path)

print(changes_to_test)