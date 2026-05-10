new_branch_name = input().strip()

git_command = "git branch"

full_command = f"{git_command} {new_branch_name}"

print(full_command)
