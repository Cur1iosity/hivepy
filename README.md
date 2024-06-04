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
### API work modes
There are three available modes for the HiveApi:
- (**json**) returns raw json response
- (**raw_items**) returns raw json response with items only
- (**object** [default]) returns parsed json response as object

### Simple HiveClient
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
    # hive.mode = 'json'  # Set mode
    
    # Getting projects and its issues
    hive.get_projects()
    hive.get_project(project_id='some-project-id')
    hive.get_issues(project_id='some-project-id')

    # Download binary file
    hive.get_file(project_id='some-project-id', file_id='some-file-id')


if __name__ == "__main__":
    main()


```
