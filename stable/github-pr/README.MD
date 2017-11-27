# GitHub Pull Request Codefresh Plugin

Creates a new pull request in GitHub

## Environment Variables

- `GITHUB_TOKEN`: token for access to GitHub
- `GITHUB_REPO_OWNER`: name of repo owner
- `GITHUB_REPO_NAME`: name of repo
- `HEAD`: The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace head with a user like this: username:branch
- `BASE`: The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository.
- `TITLE`: The title of the pull request
