"""
Extract DNS query names from PCAP file.

Category: Forensics > Network

Description:
    Parses a PCAP file and extracts all DNS query names. Useful for CTF
    challenges where data is exfiltrated via DNS queries or subdomains.

Usage:
    python pcap_extract_dns_query.py

Dependencies:
    - pyshark
    - tshark (Wireshark CLI)
"""
import pyshark

def extract_dns_requests(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter="dns")
    
    dns_requests = []
    
    for packet in cap:
        try:
            if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
                dns_requests.append(packet.dns.qry_name)
        except AttributeError:
            continue
    
    cap.close()
    return dns_requests

pcap_path = "query.pcap"
dns_queries = extract_dns_requests(pcap_path)

for query in dns_queries:
    print(query)
