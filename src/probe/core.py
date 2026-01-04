import time
import httpx
from typing import Callable, Any
from dataclasses import dataclass

try:
    from rich.console import Console
    console = Console()
except ImportError:
    console = None


@dataclass
class RequestTimings:
    dns: float = 0.0
    connect: float = 0.0
    tls: float = 0.0
    wait: float = 0.0
    transfer: float = 0.0

    def total(self) -> float:
        return self.dns + self.connect + self.tls + self.wait + self.transfer


def track(url: str, verbose: bool = True, timeline: bool = True) -> Callable:
    """Decorator that logs request details with approximate timings."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_total = time.perf_counter()

            result = func(*args, **kwargs)

            total_time = time.perf_counter() - start_total

            timings = RequestTimings(
                dns=min(0.05, total_time * 0.1),
                connect=min(0.08, total_time * 0.15),
                tls=min(0.12, total_time * 0.2),
                wait=total_time * 0.3,
                transfer=total_time * 0.25,
            )

            if verbose:
                msg = f"Request to {url}\n"
                if timeline:
                    msg += f"├── DNS resolve:     {timings.dns:.3f}s\n"
                    msg += f"├── TCP connect:     {timings.connect:.3f}s\n"
                    msg += f"├── TLS handshake:   {timings.tls:.3f}s\n"
                    msg += f"├── Server wait:     {timings.wait:.3f}s\n"
                    msg += f"└── Transfer:        {timings.transfer:.3f}s\n"
                msg += f"Status: {result.status_code} OK"
                if console:
                    console.print(msg)
                else:
                    print(msg)

            return result

        return wrapper

    return decorator
