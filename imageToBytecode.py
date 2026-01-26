#!/usr/bin/env python3

"""
Utility script to convert an image file to Python bytecode.
This is used to embed the tray icon image directly in the teainit.py script.
"""


def image_to_bytecode():
    """Convert tea.png to Python bytecode representation."""
    with open("/home/michael/Repository/Teainit/tea.png", 'rb') as file:
        bytecode = file.read()
    print("")
    print(bytecode)
    print("")


def main():
    """Main entry point for the script."""
    image_to_bytecode()


if __name__ == '__main__':
    main()
