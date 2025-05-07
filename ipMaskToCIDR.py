import argparse

def netmask_to_cidr(netmask):
    """Converts a netmask to CIDR notation."""
    return sum([bin(int(x)).count("1") for x in netmask.split(".")])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert IP and subnet mask to CIDR notation")
    parser.add_argument("--ipAddress", required = True, help="IP address to convert to CIDR." )
    parser.add_argument("--netmask", required = True, help="Subnet mask in dotted decimal format (e.g., 255.255.255.0)")

    args = parser.parse_args()

    cidr = netmask_to_cidr(args.netmask)

    print(f"{args.ipAddress}/{cidr}")
