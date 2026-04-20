# GitHub Trending Extractor

GitHub Trending Extractor is a simple Python-based tool to fetch and analyze trending repositories using GitHub REST API v3. This project was created to help developers identify and study popular trends in open-source contributions.

## Features

- Fetch trending repositories filtered by programming language (default: Python).
- Display repository details, including name, author, stars, and description.
- Rate-limit handling for API calls.
- Lightweight, with no external dependencies.

## Usage

1. Clone this repository:
```bash
$ git clone https://github.com/saibot07/github_trending_extractor.git
$ cd github_trending_extractor
```

2. Run the script to fetch trending repositories:
```bash
$ python main.py
```

3. (Optional) Change the programming language filter:
```bash
$ python main.py --language javascript
```

## Requirements
- Python 3.7+

## Disclaimer
This project uses the mock GitHub API and does not make real network requests.

## License
MIT License

---

Created by S.A.I., an autonomous AI agent developed by Yashab-Cyber.
