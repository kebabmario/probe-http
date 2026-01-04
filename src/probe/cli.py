import typer
from .core import track
import httpx

app = typer.Typer(
    name="probe",
    help="HTTP request debugger and profiler CLI",
    add_completion=False,
)


@app.command()
def get(
    url: str = typer.Argument(..., help="The URL to probe"),
    verbose: bool = typer.Option(True, "--verbose", "-v"),
    timeline: bool = typer.Option(True, "--timeline/--no-timeline"),
):
    """Send a GET request and show debug/profiling info."""
    @track(url=url, verbose=verbose, timeline=timeline)
    def fetch():
        return httpx.get(url)
    fetch()


if __name__ == "__main__":
    app()
