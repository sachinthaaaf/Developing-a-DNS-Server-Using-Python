# DNS Server Implementation

## Overview
This project involves the implementation of a DNS server using Python. The DNS server supports basic DNS functions and is capable of handling A and CNAME queries. The main goal of this project is to provide an easy-to-use yet functional DNS server that facilitates the conversion of human-readable domain names into IP addresses.

## Features
- **Support for A and CNAME records**: Users can query the DNS server to find IP addresses for specified hostnames or resolve canonical names for aliases.
- **Concurrent query handling**: The server can handle multiple DNS queries simultaneously using threading.
- **Real-time IP address retrieval**: The server uses `socket.gethostbyname` to get real-time IP addresses for A requests.
- **CNAME resolution**: The server resolves canonical names for CNAME queries using a predefined dictionary of CNAME mappings.
- **UDP socket communication**: DNS requests are exchanged between the client and server using UDP sockets.

## Functions
- **`cnames(canonical_name)`**: Contains the dictionary of specified CNAME mappings.
- **`handle_dns_query(data, client_address)`**: Handles incoming DNS queries, differentiating between A and CNAME records, and responds accordingly.
- **`dns_server()`**: Listens for incoming UDP packets, creates threads to handle queries simultaneously, and can be interrupted using the keyboard.

## Setup and Usage
1. **Clone the Repository**
   ```
   git clone https://github.com/yourusername/dns-server.git
   cd dns-server
   ```

2. **Run the DNS Server**
   ```
   python dns_server.py
   ```

3. **Run the DNS Client**
   ```
   python dns_client.py
   ```

4. **Query the DNS Server**
   - To query an A record:
     ```
     Enter hostname: example.com
     Record type: A
     ```
   - To query a CNAME record:
     ```
     Enter hostname: alias.example.com
     Record type: CNAME
     ```

## Summary
This DNS server project has provided practical experience in threading, network programming, and DNS query handling. It highlights the importance of understanding concurrent query processing, the Domain Name System, and the use of threading in Python. Through this project, the theoretical concepts of networking and programming have been applied in a real-world context, bridging the gap between abstract knowledge and practical application.

## Reflections
Developing this DNS server has deepened my understanding of networked systems and the challenges associated with maintaining their responsiveness. The practical experience gained has enhanced my knowledge of threading, error handling, and server programming. This project has been instrumental in translating theoretical knowledge into practical solutions, preparing me for real-world challenges in the field of networking and cybersecurity.

## Acknowledgments
Special thanks to the course team for the imense support, which has been a valuable learning experience in network programming and DNS server implementation.


