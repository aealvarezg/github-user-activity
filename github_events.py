# Count the commits made in this event
def push_event(repo, payload):
    commits = payload.get("commits", [])
    num_commits = len(commits)
    return f"{num_commits} commit(s) in {repo}"

# Get the type of the created object
def create_event(repo, payload):
    created_object = payload.get("ref_type", "object")
    return f"Create {created_object} in {repo}"

# Get the type of deleted object
def delete_event(repo, payload):
    deleted_object = payload.get("ref_type", "object")
    return f"Delete {deleted_object} in {repo}"

# Summarize comment in an issue
def issue_comment_event(repo):
    return f"Commented on an issue in {repo}"

# Get the pull request action
def pull_request_event(repo, payload):
    pr_action = payload.get("action", "Unknown action")
    return f"{pr_action.capitalize()} a pull request in {repo}"

# Summarize a repository fork
def fork_event(repo):
    return f"Forked repository {repo}"

# Summarize when a user marks a repository as "watched"
def watch_event(repo):
    return f"Marked repository {repo} as 'watched'"

# Summarize the publication of a new version
def release_event(repo, payload):
    version = payload.get("tag_name", "Unknown version")
    return f"Published version {version} to {repo}"

# Summarize when an issue is opened, closed, or updated.
def issues_event(repo, payload):
    action = payload.get("action", "Unknown action")
    return f"{action.capitalize()} an issue in {repo}"

# Summarize when reviewing a pull request.
def pull_request_review_event(repo):
    return f"Reviewed a pull request in {repo}"

# Summarize when a contributor is added or removed from a repository.
def member_event(repo, payload):
    action = payload.get("action", "Unknown action")
    return f"{action.capitalize()} a member in {repo}"

# Summarize when a private repository becomes public.
def public_event(repo):
    return f"Made {repo} public"

# Summarize when editing a Wiki page
def gollum_event(repo):
    return f"Updated the wiki in {repo}"
