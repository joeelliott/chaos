import curses
import time
from scapy.all import sniff, ARP

def get_clients(packet, clients):
    if ARP in packet and packet[ARP].op in (1, 2):  # ARP Request or Reply
        client_ip = packet[ARP].psrc
        client_mac = packet[ARP].hwsrc
        clients[client_ip] = client_mac

def display(screen):
    curses.curs_set(0)  # Hide cursor
    screen.nodelay(True)  # Non-blocking input
    clients = {}

    while True:
        screen.clear()
        screen.addstr(0, 0, "IP Address\tMAC Address\n", curses.A_BOLD)
        line = 1

        # Capture packets in real-time and update clients dictionary
        sniff(prn=lambda packet: get_clients(packet, clients), store=False, count=10)

        # Display clients
        for ip, mac in clients.items():
            screen.addstr(line, 0, f"{ip}\t{mac}\n")
            line += 1

        screen.refresh()

        # Exit on 'Q' key press
        if screen.getch() == ord('q'):
            break

        time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(display)
