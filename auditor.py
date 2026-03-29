import os
import subprocess

def check_open_ports():
    print("[+] Checking Open Ports...")
    try:
        # يظهر المنافذ المفتوحة في النظام
        result = subprocess.check_output("netstat -tuln", shell=True).decode()
        print(result)
    except Exception as e:
        print(f"[-] Error: {e}")

def check_sensitive_files():
    print("[+] Checking Security Permissions of /etc/passwd...")
    if os.path.exists("/etc/passwd"):
        stats = os.stat("/etc/passwd")
        # استخراج تصاريح الملف بشكل رقمي
        print(f"File Permissions: {oct(stats.st_mode)[-3:]}")
    else:
        print("[-] File /etc/passwd not found.")

if __name__ == "__main__":
    print("=== Azoth-Engineer Security Auditor Tool ===")
    check_open_ports()
    check_sensitive_files()
