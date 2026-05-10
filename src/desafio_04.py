branch_name = input().strip()

git_command = "git checkout"

full_command = f"{git_command} {branch_name}"

print(full_command)
