import subprocess
import argparse
import sys
import re

def check_website_reachability(url):
    """
    Checks the reachability of a website using curl.

    Args:
        url (str): The URL of the website to check.

    Returns:
        str: The HTTP status code from the curl output, or None on error.
    """
    #print("DEBUG: check_website_reachability() function called")
    try:
        # Construct the curl command to get only the HTTP status code.
        command = ['curl', '-sI', url, " | grep HTTP/2"]

        # Run the curl command and capture the output.
        process = subprocess.run(command, capture_output=True)

        #  The output of curl is now ONLY the status code.
        return str(process.stdout.decode('utf-8').splitlines()[0])

    except FileNotFoundError:
        print("Error: curl command not found.  Please make sure curl is installed and in your system's PATH.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while checking {url}: {e}")
        return None

def main():
    """
    Parses the command-line arguments and calls the reachability check function.
    """
    # Create an argument parser.
    parser = argparse.ArgumentParser(description="Check website reachability using curl.")
    parser.add_argument("--url", help="The URL of the website to check.")
    args = parser.parse_args()
    url = args.url

    # Check the website reachability.
    output = check_website_reachability(url)

    print(output)

if __name__ == "__main__":
    main()
