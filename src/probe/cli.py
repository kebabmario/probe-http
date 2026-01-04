import typer
from .core import track
import httpx

app = typer.Typer(
    name="probe",
    help="HTTP request debugger and profiler",
    add_completion=False,
)

@app.callback(invoke_without_command=True)
def main(
    url: str = typer.Argument(..., help="The URL to probe"),
    verbose: bool = typer.Option(True, "--verbose", "-v", help="Show detailed output"),
    timeline: bool = typer.Option(True, "--timeline", help="Show phase timeline"),
):
    """Probe a URL and display debug/profiling info."""
    @track(verbose=verbose, timeline=timeline)
    def fetch():
        return httpx.get(url)
    fetch()

if __name__ == "__main__":
    app()
