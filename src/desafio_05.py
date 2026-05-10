branch_to_merge = input().strip()

git_command = "git merge"

full_command = f"{git_command} {branch_to_merge}"

print(full_command)
