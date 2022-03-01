def defangIPaddr(address):
    address = address.replace(".", "[.]");
    return address;