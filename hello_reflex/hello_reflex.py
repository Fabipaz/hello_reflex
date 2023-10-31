"""Welcome to Reflex!."""

from hello_reflex import styles

# Import all the pages.
from hello_reflex.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
