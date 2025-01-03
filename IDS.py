import tkinter as tk
from tkinter import messagebox
from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time
import threading
from datetime import datetime

# Predefined suspicious IPs and ports (Example data)
SUSPICIOUS_IPS = ['192.168.1.1', '127.0.0.1', '8.8.8.8', '1.1.1.1']# Add your own suspicious IPs
SUSPICIOUS_PORTS = [80, 443, 21, 22, 23, 3389, 25] # Add ports you want to monitor

# List to hold detection data
detected_threats = []

# Function to detect suspicious packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if TCP in packet or UDP in packet:
            src_port = packet.sport
            dst_port = packet.dport

            # Check if the packet matches suspicious IPs or ports
            if ip_src in SUSPICIOUS_IPS or ip_dst in SUSPICIOUS_IPS or src_port in SUSPICIOUS_PORTS or dst_port in SUSPICIOUS_PORTS:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                alert_message = f"Suspicious activity detected: {ip_src} -> {ip_dst} (Port: {src_port} -> {dst_port})"
                print(alert_message)

                # Append threat information to the list
                detected_threats.append({
                    'Timestamp': timestamp,
                    'Source IP': ip_src,
                    'Destination IP': ip_dst,
                    'Source Port': src_port,
                    'Destination Port': dst_port
                })

# Function to start sniffing network traffic
def start_sniffing(duration):
    sniff(timeout=duration, prn=packet_callback, store=False)

# Function to save results to an Excel file (even if no threats are detected)
def save_to_excel():
    filename = f"IDS_Log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    if not detected_threats:
        # If no suspicious activity is detected, log that as well
        detected_threats.append({
            'Timestamp': 'N/A',
            'Source IP': 'No threats detected',
            'Destination IP': 'No threats detected',
            'Source Port': 'N/A',
            'Destination Port': 'N/A'
        })
    
    df = pd.DataFrame(detected_threats)
    df.to_excel(filename, index=False)
    messagebox.showinfo("Save Log", f"Log saved to {filename}")

# Function to start the IDS
def start_ids():
    try:
        duration = int(duration_entry.get())
        if duration <= 0:
            raise ValueError("Duration must be positive")

        # Clear previous detection results
        detected_threats.clear()

        # Start sniffing in a separate thread to keep the GUI responsive
        threading.Thread(target=start_sniffing, args=(duration,)).start()
        messagebox.showinfo("IDS", f"Started network scanning for {duration} seconds...")

        # Delay to save the results after sniffing completes
        root.after(duration * 1000, save_to_excel)

    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Tkinter GUI setup
root = tk.Tk()
root.title("Cross-Platform Intrusion Detection System (IDS)")

# GUI Labels and Entries
tk.Label(root, text="Enter scan duration (seconds):").pack(pady=10)
duration_entry = tk.Entry(root)
duration_entry.pack(pady=5)

# Start Button
start_button = tk.Button(root, text="Start IDS", command=start_ids)
start_button.pack(pady=20)

# Run the Tkinter loop
root.mainloop()
