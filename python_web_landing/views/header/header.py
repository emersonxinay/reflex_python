import reflex as rx


def header() -> rx.Component:
    return rx.vstack(

        rx.avatar(fallback="EX", size="9"),
        rx.text("@emersonxinay"),
        rx.text("Hola 👋  mi nombre es Emerson Espinoza ", height="40px"),
        rx.text(
            "Soy Ingeniero de Sistemas con más de 5 años de experiencia en desarrollo web. Mi plan incluye fortalecer mis fundamentos de programación, dominar HTML, CSS y JavaScript, y ampliar mis habilidades en Ruby on Rails, Python (Django y Flask) y PostgreSQL. Busco mejorar en la creación y consumo de APIs, así como en el despliegue y gestión de aplicaciones. Mi compromiso es seguir aprendiendo y creciendo en el campo del desarrollo fullstack"),
        paddingx="20px",
        paddingy="20px",
        align="center"
    )
