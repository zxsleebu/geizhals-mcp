"""Console entry point for installs (uvx, pip): runs upstream's main.py.

Defaults to stdio, which is what MCP hosts that start the server want;
pass --http to get upstream's streamable-HTTP mode on 127.0.0.1:8000.
"""
import runpy
import sys


def main() -> None:
    args = sys.argv[1:]
    if "--http" in args:
        args.remove("--http")
    elif "--stdio" not in args:
        args.append("--stdio")
    sys.argv = [sys.argv[0], *args]
    runpy.run_module("main", run_name="__main__")


if __name__ == "__main__":
    main()
