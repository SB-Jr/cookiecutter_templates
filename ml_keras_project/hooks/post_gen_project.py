import os

print('Starting Post Hook!!')
if '{{ cookiecutter.initialize_git }}' == 'Yes':
    os.system('git init')
    if '{{ cookiecutter.initialize_git_remote_link }}' == 'Yes':
        print('Adding git remote links')
        os.system('git remote add origin {{ cookiecutter.github_repo_link }}')
        os.system('git remote set-url origin --add {{ cookiecutter.gitlab_repo_link }}')

print('Done!!')