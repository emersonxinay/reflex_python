import reflex as rx
from python_web_landing.components.link_button import link_button

# funcion con botones


def links():
    return rx.vstack(
        link_button("Linkedin", "http://www.linkedin.com"),
        link_button("Github", "http://github.com/linkedin"),
        link_button("Twitter", "http://twitter.com/"),
        link_button("Instagram", "http://instagram.com/"),
        link_button("Facebook", "http://www.facebook.com"),
        link_button("Youtube", "http://www.youtube.com/watch"),
        align="center"
    )
