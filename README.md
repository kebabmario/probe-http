# probe-http

Lightweight HTTP request debugger and profiler for Python.

Shows detailed request timings broken down by phase  
(DNS lookup, TCP connect, TLS handshake, server wait, data transfer),  
status code, and more — perfect for figuring out why an API call is slow or failing.

## Features
- Easy decorator to wrap your HTTP calls
- Simple CLI for quick testing
- Phase-by-phase timing breakdown (MVP uses simulated values; real timings coming soon)
- Pretty, colored tree-style output (optional via `rich`)
- Works with sync and async code
- Very few dependencies

## Installation

Install the base package:

```bash
pip install probe-http
```

For the nice colored output (highly recommended):

```bash
pip install "probe-http[rich]"
```

That's it — you're ready to start debugging HTTP requests!

## Quick Start

### As a library (decorator)

```python
from probe import track
import httpx

@track(verbose=True, timeline=True)
def fetch_data():
    return httpx.get("https://httpbin.org/get")

fetch_data()
```

Expected output (with rich installed):

```
Request to https://httpbin.org/get
├── DNS resolve:     0.032s
├── TCP connect:     0.045s
├── TLS handshake:   0.120s
├── Server wait:     0.180s
└── Transfer:        0.250s
Status: 200 OK
```

### As a CLI tool

```bash
# Basic probe
probe get https://httpbin.org/get

# With more detail
probe get https://api.github.com --verbose
```

---

## Roadmap
- Real per-phase timings using httpx transport hooks
- Support for requests and aiohttp
- Export to JSON or HAR format
- Proxy mode for capturing traffic
- Custom output styles

## Contributing
Contributions welcome!

1. Fork the repo
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add your feature'`)
4. Push (`git push origin feature/your-feature`)
5. Open a Pull Request

## License
MIT License — see the [LICENSE](LICENSE) file for details.

Made with ❤️ by Kebabmario