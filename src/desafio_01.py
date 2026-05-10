repository_url = input().strip()

git_command = "git clone"

full_command = f"{git_command} {repository_url}"

print(full_command)
