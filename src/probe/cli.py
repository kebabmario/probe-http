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
    verbose: bool = typer.Option(True, "--verbose/--no-verbose", help="Show detailed output"),
    timeline: bool = typer.Option(True, "--timeline/--no-timeline", help="Show phase timeline"),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON instead of text"),
):
    """Probe a URL with GET and show timings + status."""
    @track(url=url, verbose=verbose, timeline=timeline, json_output=json_output)
    def fetch():
        return httpx.get(url)

    fetch()


if __name__ == "__main__":
    app()
