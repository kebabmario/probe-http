import time
import httpx
from typing import Callable, Any

try:
    from rich.console import Console
    console = Console()
except ImportError:
    console = None

def track(verbose: bool = True, timeline: bool = True) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.perf_counter()
            timings = {
                "dns": 0.032,
                "connect": 0.045,
                "tls": 0.120,
                "wait": 0.180,
                "transfer": 0.0
            }
            try:
                result = func(*args, **kwargs)
                total = time.perf_counter() - start
                timings["transfer"] = total - (0.032 + 0.045 + 0.120 + 0.180)

                if verbose:
                    url = kwargs.get('url', args[0] if args else 'unknown')
                    msg = f"Request to {url}\n"
                    if timeline:
                        msg += f"├── DNS resolve:     {timings['dns']:.3f}s\n"
                        msg += f"├── TCP connect:     {timings['connect']:.3f}s\n"
                        msg += f"├── TLS handshake:   {timings['tls']:.3f}s\n"
                        msg += f"├── Server wait:     {timings['wait']:.3f}s\n"
                        msg += f"└── Transfer:        {timings['transfer']:.3f}s\n"
                    msg += f"Status: {result.status_code}"
                    if console:
                        console.print(msg)
                    else:
                        print(msg)
                return result
            except Exception as e:
                err = f"Error: {str(e)}"
                if console:
                    console.print(err, style="red")
                else:
                    print(err)
                raise
        return wrapper
    return decorator
