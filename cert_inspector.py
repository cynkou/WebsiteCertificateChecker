import socket
import ssl


PORT = 443

def get_certificate(host, port):
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname = host) as ssock:
            cert = ssock.getpeercert()

    issuer = cert.get("issuer",())
    subject = cert.get("subject",())

    issuer_organization_name = next(
        value
        for group in issuer
            for key, value in group
                if key == "organizationName"
    ),
    "Not found"

    subject_common_name = next(
        value
        for group in subject
            for key, value in group
                if key == "commonName"
    ),
    "Not found"
    
    print(f"Certificate for {host}:")
    print(f"Subject: {subject_common_name}")
    print(f"Issuer: {issuer_organization_name}")
    print(f"Experation date: {cert.get('notAfter')}")


def main():
    host = input("Enter a host name (ex. google.com): ").strip()

    if not host:
        print("Input cannot be empty")
        return

    get_certificate(host, PORT)


if __name__ == "__main__":
    main()


