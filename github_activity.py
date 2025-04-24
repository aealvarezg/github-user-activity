import requests
import github_events as ge
import argparse 
from collections import defaultdict



# Gets a GitHub user's recent activity using the GitHub API.
def get_recent_activity(user):

    URL = f"https://api.github.com/users/{user}/events"

    try:
        response = requests.get(URL)
        response.raise_for_status()

        events = response.json()

        if not events:
            print(f"No recent activity found for user {user}.")
            return []
        
        return events

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error in the request: {req_err}")
    except ValueError:
        print("Invalid response from the API.")
    
    return []

# Groups events by type and generates a readable summary.
def group_events(events):
    
    resume = defaultdict(list)

    for event in events:
        type = event.get("type", "Unknown type")
        repo = event.get("repo", {}).get("name", "Unknown repository")
        payload = event.get("payload", {})

        if type == "PushEvent":
            resume[type].append(ge.push_event(repo, payload))
        elif type == "CreateEvent":
            resume[type].append(ge.create_event(repo, payload))
        elif type == "DeleteEvent":
            resume[type].append(ge.delete_event(repo, payload))
        elif type == "IssueCommentEvent":
            resume[type].append(ge.issue_comment_event(repo))
        elif type == "PullRequestEvent":
            resume[type].append(ge.pull_request_event(repo, payload))
        elif type == "ForkEvent":
            resume[type].append(ge.fork_event(repo))
        elif type == "WatchEvent":
            resume[type].append(ge.watch_event(repo))
        elif type == "ReleaseEvent":
            resume[type].append(ge.release_event(repo))
        elif type == "IssuesEvent":
            resume[type].append(ge.issues_event(repo, payload))
        elif type == "PullRequestEvent":
            resume[type].append(ge.pull_request_event(repo))
        elif type == "MemberEvent":
            resume[type].append(ge.member_event(repo, payload))
        elif type == "PublicEvent":
            resume[type].append(ge.public_event(repo))
        elif type == "GollumEvent":
            resume[type].append(ge.gollum_event(repo))
        else:
            resume[type].append(f"Event in {repo}")
        
    return resume

# Displays the grouped summary of events in a readable format.
def show_resume(resume):
    if not resume:
        print("There is no activity to show.")
    
    print("Activity Summary:\n")
    for type, actions in resume.items():
        print(f"- {type}:")
        for action in actions:
            print(f"  - {action}")
        print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Get a GitHub user's recent activity")
    parser.add_argument("user", type=str, help="GitHub username")

    args = parser.parse_args()
    
    events = get_recent_activity(args.user)
    resume = group_events(events)
    show_resume(resume) 

if __name__ == "__main__":
    main()