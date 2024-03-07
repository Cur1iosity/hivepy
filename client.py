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
    print(hive.get_groups())
    print(hive.get_group('cb60ba78-bd28-4c7c-8a46-dbb840127986'))
    print(hive.get_editable_projects_meta())


if __name__ == "__main__":
    main()
