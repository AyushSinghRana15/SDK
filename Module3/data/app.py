# Copyright 2026
# This file is part of the project.

"""Main application entry point."""

import sys
from utils.helpers import format_output
from utils.config import load_config

def main():
    config = load_config()
    message = f"App v{config.get('version', '0.1')} starting..."
    print(format_output(message))

if __name__ == "__main__":
    main()
