import uuid
from typing import Dict

from hivepy import Hive


def main() -> None:
    """Main function."""
    auth = {
        'url': 'http://192.168.1.144',
        'username': 'root@ro.ot',
        'password': '65Beforeth!',
        'proxy': 'http://127.0.0.1:8080'
    }

    hive: Hive = Hive().connect(**auth)
    # print(hive.get_users())
    # print(hive.get_groups())
    # print(hive.get_projects())
    # print(hive.get_project(uuid.UUID('0be683ea-98be-4123-a64a-2a3029c83798')))



if __name__ == "__main__":
    main()
