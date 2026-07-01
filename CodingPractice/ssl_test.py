import socket
import ssl
import certifi

def ssl_connect_python(host, port=443):
    # Create a default SSL context with system CAs and verification
    # certifi helps ensure an up-to-date CA list across different systems
    context = ssl.create_default_context(cafile=certifi.where())
    
    try:
        # Create a standard socket
        with socket.create_connection((host, port)) as sock:
            # Wrap the socket in an SSL/TLS context
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                print(f"Connected to {host}:{port} via {ssock.version()}")
                # You can perform further operations like sending/receiving data
                # For example, sending an HTTP GET request
                # ssock.sendall(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\nConnection: close\r\n\r\n")
                # response = ssock.recv(4096)
                # print(response.decode())
                
                # Get peer certificate information
                cert = ssock.getpeercert()
                print("\n--- Certificate Information ---")
                # print(cert) # Use this to print the full dictionary
                print(f"Subject: {cert['subject']}")
                print(f"Issuer: {cert['issuer']}")
                print("-------------------------------\n")
                
                return ssock

    except ssl.SSLError as e:
        print(f"SSL Error: {e}")
    except socket.error as e:
        print(f"Socket Error: {e}")

# Example usage:
ssl_connect_python("www.google.com", 443)
