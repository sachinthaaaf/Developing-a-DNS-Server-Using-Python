# Sachintha Fernando
# BSCP|CS|62|113

import socket

def dns_client():
    while True:
        # User input for hostname/alias and record type (A or CNAME)
        hostname = input("Enter hostname/alias: ")
        record_type = input("Enter record type (A or CNAME): ")

        # Creating a query string in the format "hostname,record_type"
        query = f"{hostname},{record_type}"

        # Sending the DNS query to the server
        client_socket.sendto(query.encode('utf-8'), server_address)

        # Receiving and displaying the DNS response
        data, _ = client_socket.recvfrom(1024)
        print(data.decode('utf-8'))

        # Prompting the user to continue or exit
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    # Creating a UDP socket for the DNS client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('127.0.0.1', 53)

    try:
        # Starting the DNS client
        dns_client()
    finally:
        # Closing the socket when done
        client_socket.close()
