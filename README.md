# GeometryDash.py

A simple API wrapper for Geometry Dash 2.1 written in Python.

## Key Features

- Modern Pythonic API using `async` and `await` syntax
- High coverage of the supported Geometry Dash API

## Installing

**Python 3.6 or higher is required**

```shell
pip install geometrydash
```

## Examples

### Level Example
```python
import geometrydash as gd

level = await gd.search_level("zodiac")
level.featured  # True
level.coins  # 0
```

### Profile Example
```python
import geometrydash as gd

user = await gd.search_user("robtop")
user.name  # 'RobTop'
user.moderator  # 'elder'
```

## Licence

GNU General Public Licence v3.0

## Links

- [Geometry Dash API]('https://gdbrowser.com/api')
