# HivePy
Unofficial flexible library for [HexWay Hive](https://hexway.io/hive/) Rest API.

#### Tested on HexWay Hive 0.62.8

## Installation
```bash
pip install hw-hivepy
```

## Dependencies

- pydantic ~= 2.4
- requests ~= 2.31.0

## Usage

```python
from hivepy import HiveApi


def main() -> None:
    """Main function."""
    auth = {
        'url': 'http://127.0.0.1',
        'username': 'user',
        'password': 'password',
    }

    hive: HiveApi = HiveApi().connect(**auth)

if __name__ == "__main__":
    main()

```
