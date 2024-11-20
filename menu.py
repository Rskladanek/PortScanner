from modules.portscanner import PortScanner

class Menu:

    """
    Represents the main menu of the Port Scanner application.
    """

    def __init__(self):
        self.running = True
        self.PS = None
        self.get_target_ip()

    def get_target_ip(self):
        while True:
            ip = input("Enter the IP address to be scanned: ")
            if self.validate_ip(ip):
                self.PS = PortScanner(ip)
                break
            else:
                print("Invalid IP address. Please enter a valid IP.")

    @staticmethod
    def validate_ip(ip):
        import socket
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False

    @staticmethod
    def broadcast():
        print(r"""
            ______               _    _____                                        
            | ___ \             | |  /  ___|                                       
            | |_/ /  ___   _ __ | |_ \ `--.   ___   __ _  _ __   _ __    ___  _ __ 
            |  __/  / _ \ | '__|| __| `--. \ / __| / _` || '_ \ | '_ \  / _ \| '__|
            | |    | (_) || |   | |_ /\__/ /| (__ | (_| || | | || | | ||  __/| |   
            \_|     \___/ |_|    \__|\____/  \___| \__,_||_| |_||_| |_| \___||_|                                                                                                                                
        """)

    def choose_option(self, interaction: int):
        if interaction == 1:
            self.tcp_port_scan()
        elif interaction == 2:
            self.udp_port_scan()
        elif interaction == 3:
            self.show_open_ports()
        elif interaction == 4:
            self.change_target_ip()
        elif interaction == 5:
            self.exit()
        else:
            print("Invalid option. Please choose a valid one.")

    def tcp_port_scan(self):
        try:
            start_port = int(input("Enter the starting port for TCP scan: "))
            end_port = int(input("Enter the ending port for TCP scan: "))
            if start_port < 0 or end_port > 65535 or start_port > end_port:
                print("Invalid port range. Ports must be between 0 and 65535, and start must be ≤ end.")
                return
            self.PS.tcp_scan(start_port=start_port, end_port=end_port)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    def udp_port_scan(self):
        try:
            start_port = int(input("Enter the starting port for UDP scan: "))
            end_port = int(input("Enter the ending port for UDP scan: "))
            if start_port < 0 or end_port > 65535 or start_port > end_port:
                print("Invalid port range. Ports must be between 0 and 65535, and start must be ≤ end.")
                return
            self.PS.udp_scan(start_port=start_port, end_port=end_port)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    def show_open_ports(self):
        if self.PS.open_ports:
            print("Open ports found:")
            for port in self.PS.open_ports:
                print(f"Port {port}")
        else:
            print("No open ports found or scan not performed yet.")

    def change_target_ip(self):
        self.get_target_ip()
        print(f"Target IP changed to {self.PS.ip}")

    @staticmethod
    def options():
        print("""
              === Choose an Option ===
              1. TCP Port Scan 
              2. UDP Port Scan
              3. Show Open Ports
              4. Change Target IP
              5. Exit    
              =========================
              """)

    def run(self):
        self.broadcast()
        while self.running:
            self.options()
            try:
                choice = int(input("Select an option: "))
                self.choose_option(choice)
            except ValueError:
                print("Invalid input. Please enter a numeric option.")

    def exit(self):
        print("Exiting the Port Scanner. Goodbye!")
        self.running = False