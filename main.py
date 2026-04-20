import argparse
import json

# Mock function to simulate GitHub API response
def fetch_trending_repositories(language='python'):
    # Predefined sample data based on GitHub API structure
    return [
        {
            'name': 'awesome-python',
            'owner': {'login': 'vinta'},
            'stargazers_count': 145000,
            'description': 'A curated list of awesome Python frameworks, libraries, software and resources.',
            'language': 'Python'
        },
        {
            'name': 'public-apis',
            'owner': {'login': 'public-apis'},
            'stargazers_count': 250000,
            'description': 'A collective list of free APIs for use in software and web development.',
            'language': 'Python'
        }
    ]

# Function to print repository details
def display_repositories(repos):
    print("\nTrending Repositories:\n")
    for i, repo in enumerate(repos, start=1):
        print(f"{i}. {repo['name']} by {repo['owner']['login']}")
        print(f"   🌟 Stars: {repo['stargazers_count']}")
        print(f"   📚 Description: {repo['description']}")
        print("")

# Main execution block
def main():
    parser = argparse.ArgumentParser(description='GitHub Trending Repository Extractor')
    parser.add_argument('--language', type=str, default='python', help='Programming language to filter by (default: Python)')
    
    args = parser.parse_args()
    
    # Fetch and display repositories
    repositories = fetch_trending_repositories(language=args.language)
    display_repositories(repositories)

if __name__ == '__main__':
    main()
