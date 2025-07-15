#!/usr/bin/env python3
"""
A simple script that uses argparse to accept a single string argument,
validates if it's JSON, and prints the parsed JSON or the original string.
"""

import argparse
import json


def main():
    """Main function to parse arguments and print the string or parsed JSON."""
    # Create the parser
    parser = argparse.ArgumentParser(
        description='A script that accepts a string, validates if it\'s JSON, and prints parsed JSON or the original string'
    )
    
    # Add a single argument for the string
    parser.add_argument(
        'text',
        type=str,
        help='The string to be validated and printed (can be JSON or plain text)'
    )
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Try to parse as JSON
    try:
        # Attempt to parse the input as JSON
        parsed_json = json.loads(args.text)
        
        # If successful, print the formatted JSON
        print("Valid JSON detected. Parsed output:")
        print(json.dumps(parsed_json, indent=2))
        
    except json.JSONDecodeError:
        # If it's not valid JSON, print the original string
        print("Not valid JSON. Original string:")
        print(args.text)


if __name__ == '__main__':
    main()
