from hivepy import HiveApi


def main() -> None:
    """Main function."""
    auth = {
        'url': 'http://127.0.0.1',
        'username': 'user',
        'password': 'password',
    }

    hive: HiveApi = HiveApi().connect(**auth)

    # Getting projects and its issues
    hive.get_projects()
    hive.get_project(project_id='some-project-id')
    hive.get_issues(project_id='some-project-id')

    # Download binary file
    hive.get_file(project_id='some-project-id', file_id='some-file-id')


if __name__ == "__main__":
    main()
