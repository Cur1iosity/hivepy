from hivepy import Hive


def main() -> None:
    """Main function."""
    auth = {
        'server': 'http://127.0.0.1',
        'username': 'user',
        'password': 'password',
    }

    hive: Hive = Hive().connect(**auth)

    # Getting projects and its issues
    hive.get_projects()
    hive.get_projects(project_id='some-project-id')
    hive.get_issues(project_id='some-project-id')

    # Updating issue fields
    hive.update_issue(project_id='some-project-id', issue_id='some-issue-id', status='ready')

    # Download binary file
    hive.get_file(project_id='some-project-id', file_id='some-file-id')


if __name__ == "__main__":
    main()
