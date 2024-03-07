from typing import Dict

from hivepy import Hive


def main() -> None:
    """Main function."""
    auth = {
        'server': 'http://192.168.1.144',
        'username': 'root@ro.ot',
        'password': '65Beforeth!',
        'proxy': 'http://127.0.0.1:8080'
    }

    hive: Hive = Hive().connect(**auth)
    result: Dict = hive.get_project_groups()
    print(result)


if __name__ == "__main__":
    main()
