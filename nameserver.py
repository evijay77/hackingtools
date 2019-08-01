import dns.resolver
import socket

domain = input("Enter a Url: ")
host_ip = socket.gethostbyname(domain)
print("IP Address :",host_ip) 
answers = dns.resolver.query(domain,'NS')
print('Name Server')
for server in answers:
    print(server.target)

