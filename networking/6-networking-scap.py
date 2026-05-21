from scapy.all import IP, ICMP, sr1

# define the taget IP address

target_ip = "www.google.com"

# craft an ICMP packet (ping request)

packet = IP(dst=target_ip) / ICMP()

# send the packet and recieve responce 

response = sr1(packet, timeout=2, verbose=False)

# check if a responce was received 
if response:
    print(f"Revieved response from {response.src}")
else:
    print("No response received..")
    
    