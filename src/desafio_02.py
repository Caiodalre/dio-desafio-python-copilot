files_to_add = input().strip()

git_command = "git add"

full_command = f"{git_command} {files_to_add}"

print(full_command)
