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
    return <MyComponent message="Hello from a componen"/>