import reflex as rx


def navbar() -> rx.Component:
    return rx.hstack(

        rx.text("CompilandoCode", padding="20px"),
        position="sticky",
        bg="Blue",

        borderradius="10px",
        color="white",
        z_index="999"
    )
