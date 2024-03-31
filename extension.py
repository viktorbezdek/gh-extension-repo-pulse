import sys

from cleo.application import Application
from cleo.io.io import IO
from cleo.io.inputs.string_input import StringInput
from cleo.commands.command import Command

def run(args=None):
    # Set your name and version here.
    application = Application(name='Repo Pulse', version='0.1.0')
    # add your commands here.
    application.add(RepoPulse())

    # below here we run. You don't need to modify this.
    if args:
        input = StringInput(args)
        input.set_stream(sys.stdin)
        application.run(input)
    else:
        application.run()
    
class RepoPulse:
    name = "repo-pulse"
    description = "Get pulse of a GitHub repository."

    def handle(self):
        api_url = f"https://api.github.com/repos/{repo_url}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        if "GITHUB_TOKEN" in os.environ:
            headers["Authorization"] = f"token {os.environ['GITHUB_TOKEN']}"

        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            repo_data = response.json()

            name = repo_data["name"]
            description = repo_data["description"]
            language = repo_data["language"]
            license_name = (
                repo_data["license"]["name"] if repo_data["license"] else "Not available"
            )
            stargazers_count = repo_data["stargazers_count"]
            forks_count = repo_data["forks_count"]
            created_at = datetime.strptime(
                repo_data["created_at"], "%Y-%m-%dT%H:%M:%SZ"
            ).strftime("%b %d, %Y")
            updated_at = datetime.strptime(
                repo_data["updated_at"], "%Y-%m-%dT%H:%M:%SZ"
            ).strftime("%b %d, %Y")

            contributors_url = repo_data["contributors_url"]
            contributors_response = requests.get(contributors_url, headers=headers)
            contributors_count = len(contributors_response.json())

            commits_url = repo_data["commits_url"].replace("{/sha}", "")
            commits_response = requests.get(commits_url, headers=headers)
            commits_data = commits_response.json()
            commit_count = len(commits_data)

            releases_url = repo_data["releases_url"].replace("{/id}", "")
            releases_response = requests.get(releases_url, headers=headers)
            releases_count = len(releases_response.json())

            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Language: {language}")
            print(f"License: {license_name}")
            print(f"Stars: {stargazers_count}")
            print(f"Forks: {forks_count}")
            print(f"Created At: {created_at}")
            print(f"Last Updated: {updated_at}")
            print(f"Contributors: {contributors_count}")
            print(f"Commits: {commit_count}")
            print(f"Releases: {releases_count}")
        else:
            print(f"Failed to fetch repository data. Status code: {response.status_code}")        