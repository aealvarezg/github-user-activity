# GitHub User Activity

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

A command-line interface (CLI) application in Python that fetches and displays the recent activity of a GitHub user using the GitHub API.

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributions](#contributions)
7. [License](#license)

---

## Description

This project is a CLI tool that allows you to query the recent activity of a GitHub user. It uses the public GitHub API to retrieve recent events and groups them by event type for better readability.

For example, if the user has made multiple commits or created new branches, the tool will display a clear and organized summary.

This project is inspired from the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) from [Roadmap](https://www.roadmap.sh).

---

## Features

- **Grouped Summary**: Groups actions by event type (e.g., commits made, branches created, etc.).
- **Support for Multiple Event Types**: Handles events such as `PushEvent`, `CreateEvent`, `PullRequestEvent`, `ForkEvent`, etc.
- **Simple Interface**: Easy to use from the command line.
- **Unauthenticated User Friendly**: Works without authentication (within the API rate limits).

---

## Requirements

- Python 3.7 or higher
- `requests` library (installed automatically)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aealvarezg/github-user-activity.git
   cd github-user-activity
   ```

---

## Usage

Run the script from the command line, passing the GitHub username as an argument:

```bash
python github_activity.py <username>
```

For example:
```bash
python github_activity.py aealvarezg
```

### Output for a user with recent activity

```
Activity Summary:

- PushEvent:
  - 1 commit(s) in aealvarezg/github-user-activity
  - 1 commit(s) in aealvarezg/Task_Tracker_CLI
  - 1 commit(s) in aealvarezg/Task_Tracker_CLI
  - 1 commit(s) in aealvarezg/Task_Tracker_CLI
  - 1 commit(s) in aealvarezg/Task_Tracker_CLI
----------------------------------------
- CreateEvent:
  - Create repository in aealvarezg/github-user-activity
  - Create branch in aealvarezg/github-user-activity
  - Create branch in aealvarezg/Task_Tracker_CLI
  - Create repository in aealvarezg/Task_Tracker_CLI
----------------------------------------
```

### Output for a user with no activity

If the user has no recent activity, the output will be:

```
No recent activity found for the user 'username'.
```

---

## Contributions

Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Additional Notes

- **Rate Limiting**: The GitHub API has a limit of 60 requests per hour for unauthenticated users. If you plan to make many queries, consider using a personal access token to increase the limit.
- **Pagination**: This project currently does not handle pagination. If you need to process more than 30 events, you can implement pagination using the `Link` header in the API response.

---
