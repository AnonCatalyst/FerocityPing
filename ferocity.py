import subprocess
import time
import socket
import requests

MAX_TIMEOUT_ATTEMPTS = 10  # Maximum consecutive timeout attempts before trying alternative methods

def get_location(host):
    try:
        ip = socket.gethostbyname(host)
        print(f"\033[94m[+] Location info for {host}:")  # Light blue
        response = requests.get(f"http://ipinfo.io/{ip}/json")
        data = response.json()
        print(f"IP: {ip}")
        print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
        print(f"Coords: {data.get('loc')}")
    except socket.gaierror:
        print("\033[91m[!] Error resolving host.")  # Light red
    except Exception as e:
        print("\033[91m[!] Error fetching location:", e)

def icmp_ping(host):
    try:
        start_time = time.time()
        response = subprocess.run(["ping", "-c", "1", host], capture_output=True, text=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        if response.returncode == 0:
            print("\033[92m✅", end=" ")  # Light green
            print(f"ICMP Ping to {host} successful")
            print(f"Time: {elapsed_time:.4f}s")
            return True
        else:
            print("\033[91m❌", end=" ")  # Light red
            print(f"ICMP Ping to {host} failed")
            return False
    except FileNotFoundError:
        print("\033[91m❌", end=" ")  # Light red
        print("Ping command not found.")
        return False
    except Exception as e:
        print("\033[91m❌", end=" ")  # Light red
        print(f"Error performing ICMP Ping: {e}")
        return False

def udp_ping(host, port):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(2)  # Set a timeout for the UDP socket
        udp_socket.sendto(b"", (host, port))
        udp_socket.recvfrom(1024)
        udp_socket.close()
        return True
    except socket.timeout:
        return False
    except OSError as e:
        print(f"Error performing UDP Ping: {e}")
        return False

def tcp_ping(host, port):
    try:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.settimeout(2)  # Set a timeout for the TCP socket
        tcp_socket.connect((host, port))
        tcp_socket.close()
        return True
    except socket.timeout:
        return False
    except OSError as e:
        print(f"Error performing TCP Ping: {e}")
        return False

def http_ping(url):
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            print("\033[92m✅", end=" ")  # Light green
            print(f"HTTP Ping to {url} successful")
            return True
        else:
            print("\033[91m❌", end=" ")  # Light red
            print(f"HTTP Ping to {url} failed. Status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        print("\033[91m❌", end=" ")  # Light red
        print(f"Error performing HTTP Ping: {e}")
        return False

def main():
    print("\033[95m🐾 Welcome to FerocityPing! 🐾")  # Light purple
    print("""FerocityPing is a Python network utility designed to ping hosts using various methods and retrieve location information
it offers ICMP, UDP, TCP, and HTTP ping functionalities to assess connectivity and response times. """)
   
    target = input("Target to ping (e.g., example.com or IP): ")
    port = int(input("Port to ping: "))
    endless_ping = input("Endless ping? (y/n): ").lower() == 'y'

    try:
        ip = target
        if not target.replace('.', '').isdigit():
            ip = socket.gethostbyname(target)

        get_location(ip)
        print(f"\033[94m[+] Pinging {ip}...")  # Light blue
        if endless_ping:
            print("\033[93m[+] Endless ping. Press Ctrl+C to stop.")  # Light yellow
        consecutive_timeouts = 0
        while True:
            if icmp_ping(ip):
                if not endless_ping:
                    break
            else:
                print("\033[93m[+] Trying alternative methods...")  # Light yellow
                udp_success = udp_ping(ip, port)
                tcp_success = tcp_ping(ip, port)
                if udp_success:
                    print("\033[92m✅", end=" ")  # Light green
                    print(f"UDP Ping to {ip}:{port} successful")
                if tcp_success:
                    print("\033[92m✅", end=" ")  # Light green
                    print(f"TCP Ping to {ip}:{port} successful")
                if not udp_success and not tcp_success:
                    consecutive_timeouts += 1
                    if consecutive_timeouts >= MAX_TIMEOUT_ATTEMPTS:
                        print("\033[93m[+] Max consecutive timeouts. Trying ICMP again...")  # Light yellow
                        consecutive_timeouts = 0
                    else:
                        print("\033[91m❌", end=" ")  # Light red
                        print("All methods failed. Retrying...")
            time.sleep(2)
    except ValueError:
        print("\033[91m[!] Invalid port number.")  # Light red
    except subprocess.CalledProcessError:
        print("\033[91m[!] Error executing ping command.")  # Light red
    except KeyboardInterrupt:
        print("\n\033[91m[!] Ping interrupted.")  # Light red
    except Exception as e:
        print("\033[91m❌", end=" ")  # Light red
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
