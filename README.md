# GitHub Trending Extractor

This project fetches and displays trending repositories on GitHub filtered by programming language (default: Python).

## Features
- Fetch trending repositories using GitHub's REST API.
- Display repository name, owner, stars, and descriptions in a formatted console output.
- Authenticate using a GitHub personal access token for higher API rate limits.

## Prerequisites
- Python >= 3.8
- A GitHub Personal Access Token [Create token here](https://github.com/settings/tokens). Ensure it has `public_repo` permissions.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/saibot07/github_trending_extractor.git
    cd github_trending_extractor
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate # For Windows: venv\Scripts\activate
    ```

3. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Add your GitHub Personal Access Token to an `.env` file:
    ```env
    GITHUB_TOKEN=your_personal_access_token_here
    ```

5. Run the application:
    ```bash
    python main.py
    ```

## Usage
1. Upon starting the application, you will be prompted to enter a programming language.
   - Press Enter to use the default (Python).
2. View the list of trending repositories displayed in the terminal.

## Improvements
- Asynchronous API calls for faster performance.
- Build a web dashboard for visual display.
- Add unit tests for reliability.

## License
[MIT License](LICENSE)
