from typing import Annotated

import typer

from shelter.core.parse import parse_immoscout_page


app = typer.Typer(pretty_exceptions_show_locals=False)


@app.command()
def main(
    page_content: Annotated[
        str, typer.Argument(help="content of the housing ad, i.e. its raw html.")
    ]
) -> None:
    """cli for generating a nice answer to a housing ad."""

    typer.echo(parse_immoscout_page(page_content))


if __name__ == "__main__":
    app()
