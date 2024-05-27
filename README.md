<div align="center">
<img src="https://gist.githubusercontent.com/itsmeadarsh2008/2b89b1794fd67e844441273fa5dcf77b/raw/cb35ed3e3d4b3cdcf2604364152b59fb4bc0c17c/nutritious.svg" height="300">
</div>

<h1 align="center">Nutritious Litchi</h1>

**Nutritious Litchi** is a Python package that allows you to write JSX-like syntax in Python for creating HTML elements and components. It contains a CLI which is used to convert XML-JSX to Python Objects. **Feel free to use to make a web framework with this**. This started as a fork of [Packed](https://github.com/michaeljones/packed).

> [!WARNING]  
> Please note that this is project is in experimental stage. It is a fork of [Packed](https://github.com/michaeljones/packed) and has been modified and optimized.

## Installation
```
# you can use any python package manager like pip and poetry to install nutritious instead
pip install nutritious
```

## Usage

### Basic Example (located in `app/` folder)

```python
from nutritious import litchi, Element
# Element import is required even though it's not in the script.

@litchi
def render():
    return (
        <div>
            <h1>Hello, World!</h1>
            <p>This is a JSX-like syntax in Python.</p>
            <a href="https://example.com">Link</a>
        </div>
    )
```

### Custom Components

```python
from nutritious import Component, litchi

class MyComponent(Component): # type: ignore
    def render(self):
        return <div>This is a custom component with a prop: {self.props['message']}</div>

@litchi
def app():
    return <MyComponent message="Hello from a component"/>
```

# Output `dist/` folder
```python
from nutritious import litchi, Element
# Element import required even though it's not in the script.

@litchi
def render():
    return (
        Element(
            'div',
            {},
            ' ',
            Element(
                'h1',
                {},
                'Hello, World!',
            ),
            ' ',
            Element(
                'p',
                {},
                'This is a JSX-like syntax in Python.',
            ),
            ' ',
            Element(
                'a',
                {
                    'href': 'https://example.com',
                },
                'Link',
            ),
            ' ',
        )
    )

### Custom Components

from nutritious import Component, litchi

class MyComponent(Component): # type: ignore
    def render(self):
        return Element(
            'div',
            {},
            'This is a custom component with a prop: ',
            self.props['message'],
        )

@litchi
def app():
    return <MyComponent message="Hello from a component"/>
```

# How to convert to python objects? (HELP)
```
python -m nutritious -h
```
---

**Author**: A Python3-Compatible Fork of An Archived Project Called [Packed](https://github.com/michaeljones/packed) <br>
**Modified and Optimized** by [Adarsh Gourab Mahalik](https://github.com/itsmeadarsh2008)