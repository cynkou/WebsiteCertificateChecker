# WebsiteCertificateChecker

A Python-based TLS certificate inspection tool that connects to a website over HTTPS and retrieves its TLS certificate information.

## Current Features

- Establishes a TCP connection to a specified hostname on port 443.
- Creates a secure TLS connection using Python's SSL library.
- Retrieves the server's TLS certificate.
- Extracts the certificate's subject common name.
- Extracts the issuer organization.
- Displays the certificate's expiration date.
- Uses a five-second connection timeout.
- Handles missing issuer and subject attributes with fallback values.

## Project Goals

This project will eventually expand to include:

- Subject Alternative Name (SAN) extraction.
- Certificate expiration analysis and 30-day renewal warnings.
- Improved certificate verification error handling.
- Local certificate testing and automated tests.
- A Flask-based web dashboard.
- Certificate monitoring and renewal history.
