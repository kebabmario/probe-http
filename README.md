# probe-http

A lightweight CLI tool to probe HTTP endpoints and show request timings broken down by phase.

Shows approximate timings for DNS, TCP connect, TLS, server wait, and transfer — plus status code.

## Features
- Simple `probe get <url>` command
- Pretty tree output with rich (optional)
- Flags: `--verbose` / `--no-verbose`, `--timeline` / `--no-timeline`, `--json`
- Works with httpx under the hood

## Installation
```bash
pip install probe
# or with colored output (recommended)
pip install probe[rich]
```

## Usage

Basic probe:
```bash
probe https://httpbin.org/get
```

Example output:
```
Request to https://httpbin.org/get
├── DNS resolve:     0.050s
├── TCP connect:     0.080s
├── TLS handshake:   0.120s
├── Server wait:     0.300s
└── Transfer:        0.250s
Status: 200 OK
```

JSON mode:
```bash
probe https://httpbin.org/get --json
```

Silent / no timeline:
```bash
probe https://httpbin.org/get --no-verbose --no-timeline
```

Full help:
```bash
probe --help
```

## Development / Contributing
Clone and install editable:
```bash
git clone https://github.com/kebabmario/probe.git
cd probe
pip install -e .[rich]
```

Run tests/lint:
```bash
pytest
ruff check .
mypy .
```

## License
MIT License – see [LICENSE](LICENSE)

Made by Kebabmario