import typer
from .core import track
import httpx

app = typer.Typer()

@app.command()
def get(url: str):
    @track()
    def fetch():
        return httpx.get(url)
    fetch()

if __name__ == "__main__":
    app()
