import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico", padding_top="30px"),
        rx.link(f"2019 - {datetime.date.today().year} Compilando Code", href="http://compilandocode.com)",
                is_external=True),
        align="center",
    )
