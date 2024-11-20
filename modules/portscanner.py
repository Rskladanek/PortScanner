import socket

class PortScanner:

    def __init__(self, ip, timeout=2):

        """
        Initializes the PortScanner object with the target IP address and optional timeout.

        :param ip: The IP address to scan.
        :param timeout: Timeout duration in seconds (default is 2).
        """

        self.ip = ip
        self.timeout = timeout
        self.open_ports = {'TCP': [], 'UDP': []}

    def tcp_scan(self, start_port=0, end_port=1024):

        """
        Scans the specified range of TCP ports on the target IP address.

        :param start_port: Starting port number (default is 0).
        :param end_port: Ending port number (default is 1024).
        """

        total_ports = end_port - start_port + 1
        scanned_ports = 0
        print(f"Starting TCP scan on {self.ip} from port {start_port} to {end_port}...")
        for port in range(start_port, end_port + 1):
            scanned_ports += 1
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.ip, port))
                if result == 0:
                    self.open_ports['TCP'].append(port)
            print(f"Scanned {scanned_ports}/{total_ports} TCP ports.", end="\r")
        print("\nTCP scan completed.")
        if self.open_ports['TCP']:
            print(f"Open TCP ports: {self.open_ports['TCP']}")
        else:
            print("No open TCP ports found.")

    def udp_scan(self, start_port=1, end_port=1024):

        """
        Scans the specified range of UDP ports on the target IP address.

        :param start_port: Starting port number (default is 1).
        :param end_port: Ending port number (default is 1024).
        """

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Invalid port range. Ports must be between 1 and 65535, and start_port <= end_port.")
            return

        total_ports = end_port - start_port + 1
        scanned_ports = 0
        print(f"Starting UDP scan on {self.ip} from port {start_port} to {end_port}...")

        for port in range(start_port, end_port + 1):
            scanned_ports += 1
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(0.1)  # Reduced timeout for faster scanning

                try:
                    # Send an empty packet to the target port
                    sock.sendto(b'', (self.ip, port))

                    # Attempt to receive a response (unlikely with UDP)
                    # We're not expecting a response, so we can skip recvfrom
                    # or keep it with a very short timeout
                    try:
                        data, _ = sock.recvfrom(1024)
                        # If we receive data, the port is open
                        self.open_ports['UDP'].append(port)
                    except socket.timeout:
                        # No response received; port may be open or filtered
                        pass
                except Exception as e:
                    # Handle exceptions (e.g., Network is unreachable, Permission denied)
                    print(f"Error scanning port {port}: {e}")

            # Update progress
            print(f"Scanned {scanned_ports}/{total_ports} UDP ports.", end="\r")

        print("\nUDP scan completed.")
        if self.open_ports['UDP']:
            print(f"Open UDP ports (responses received): {self.open_ports['UDP']}")
        else:
            print("No open UDP ports found (no responses received).")
