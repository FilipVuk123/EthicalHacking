import argparse
import logging
import socket
import threading
from datetime import datetime

def scan_port(target, port):
    """Scans a single port on the target host."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            logging.info(f"Port {port} is open!")

def main(target, port_min, port_max):
    """Scans a range of ports on the target host."""
    logging.info(f"Scanning target: {target}")
    logging.info(f"Started: {datetime.now()}")
    threads = []
    for port in range(port_min, port_max):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    logging.info("Scan complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", help="the IP address or hostname of the target host")
    parser.add_argument("range_min", help="the min port of the target host")
    parser.add_argument("range_max", help="the max port of the target host")
    args = parser.parse_args()
    target = socket.gethostbyname(args.target)
    range_min = int(args.range_min)
    range_max = int(args.range_max)
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    main(target, range_min, range_max)
