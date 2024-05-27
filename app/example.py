from nutritious import litchi, Element
# Element import required even though it's not in the script.

@litchi
def render():
    return (
        <div>
            <h1>Hello, World!</h1>
            <p>This is a JSX-like syntax in Python.</p>
            <a href="https://example.com">Link</a>
        </div>
    )

### Custom Components

from nutritious import Component, litchi

class MyComponent(Component): # type: ignore
    def render(self):
        return <div>This is a custom component with a prop: {self.props['message']}</div>

@litchi
def app():
    return <MyComponent message="Hello from a component"/>