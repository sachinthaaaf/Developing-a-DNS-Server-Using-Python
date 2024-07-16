# Sachintha Fernando
# BSCP|CS|62|113

import socket
import threading

# Defined a dictionary to store predefined CNAME mappings
cnames = {
    'google': 'http://www.google.com',
    'youtube': 'https://www.youtube.com',
    'github': 'https://www.github.com',
    'whatsapp': 'https://www.whatsapp.com',
    'instagram': 'https://www.instagram.com',
}

# Function to handle the DNS Queries
def handle_dns_query(data, client_address):
    # Splitting the received data to extract hostname and record type
    query_data = data.decode('utf-8').split(',')
    hostname = query_data[0]
    record_type = query_data[1]

    # Handling A record queries
    if record_type.upper() == 'A':
        try:
            # Attempting to get the IP address for the provided hostname
            ip_address = socket.gethostbyname(hostname)
            response = f'DNS Output: {hostname} (A) -> {ip_address}'.encode('utf-8')
        except socket.gaierror:
            # If the hostname is not found, generating a not found response
            response = f'DNS Output: Could not find the hostname: {hostname}'.encode('utf-8')

    # Handling CNAME record queries
    elif record_type.upper() == 'CNAME':
        # Checking if the provided hostname is in the predefined CNAME mappings
        if hostname in cnames:
            url = cnames[hostname]
            response = f'DNS Output: {hostname} (CNAME) -> {url}'.encode('utf-8')
        else:
            # If the alias is not found, generate an appropriate response
            response = f'DNS Output: Could not find alias: {hostname}'.encode('utf-8')
    else:
        # If an invalid record type is provided, generate an appropriate response
        response = b'Invalid record type'

    # Sending the DNS response to the client
    server_socket.sendto(response, client_address)


def dns_server():
    # Displaying a message indicating that the DNS server is running
    print("DNS Server is running...")

    # Continuously listening for incoming DNS queries
    while True:
        try:
            # Receiving data and client address from the socket
            data, client_address = server_socket.recvfrom(1024)

            # Creating a new thread to handle the DNS query concurrently
            threading.Thread(target=handle_dns_query, args=(data, client_address), daemon=True).start()
        except KeyboardInterrupt:
            # Handling keyboard interrupt to gracefully exit the server
            break


if __name__ == "__main__":
    # Creating a UDP socket for the DNS server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Binding the socket to the localhost address and port 53
    server_socket.bind(('127.0.0.1', 53))

    try:
        # Starting the DNS server
        dns_server()
    finally:
        # Closing the socket when done
        server_socket.close()
