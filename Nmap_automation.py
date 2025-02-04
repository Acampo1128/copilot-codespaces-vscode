import os

def run_nmap_scan(target_ip):
    command = f"nmap -p- -sV {target_ip}"
    os.system(command)

if __name__ == "__main__":
    target_ip = "192.168.1.254"
    run_nmap_scan(target_ip)
