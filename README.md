# GH Extension Project Info

`gh` extension that  retrieves repository data from the GitHub API and prints statistics about the repository including name, description, language, license, stars, forks, creation date, last update date, contributors, commits, and releases. It requires the repository URL as a parameter.

## Installation

To install this extension, run:

```
gh extension install viktorbezdek/gh-extension-repo-pulse
```

## Usage

To use this extension, run:

```
gh repo-pulse <repo-url>
```

Replace `<repo-url>` with the URL of the GitHub repository you want to analyze.

For example:

```
gh repo-pulse https://github.com/octocat/Hello-World
```

This will retrieve data about the `octocat/Hello-World` repository and print out statistics.

## Output

The extension will output the following information about the repository:

- Name
- Description
- Language
- License
- Stars
- Forks
- Created
- Last
- Contributors
- Commits
- Releases

## Dependencies

This extension uses the following dependencies:

- GitHub CLI (`gh`)

Make sure you have these installed before running the extension.

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request on the GitHub repository.

## License

This project is open source under the [GNU GPL 3.0](LICENSE).