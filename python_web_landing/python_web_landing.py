import reflex as rx
from python_web_landing.components.navbar import navbar
from python_web_landing.components.footer import footer
from python_web_landing.views.header.header import header
from python_web_landing.views.links.links import links
import python_web_landing.styles.styles as styles


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WITH,
                align="center",
                margin_y="20px"

            ),
            align="center",
        ),
        footer(),
        background="linear-gradient(45deg, var(--tomato-9), var(--plum-9))",

        align="center"
    )


# para correr reflex
app = rx.App()
app.add_page(index)
app.compile()
