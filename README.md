# DataVIA_Connect

This Python script connects to the Geoplace DataVIA API and retrieves street data for a specified USRN (Unique Street Reference Number) using a Basic connection to the Geoplace DataVIA service.

## Features

- Connects to the Geoplace DataVIA API
- Retrieves street data for a given USRN
- Uses Basic authentication for API access

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/KFergusonUK/DataVIA_Connect.git
    ```
2. Navigate to the project directory:
    ```bash
    cd DataVIA_Connect
    ```

## Usage

1. Install the required dependencies:
    ```bash
    pip install requests
    ```
2. Update the script with your Geoplace DataVIA API credentials.
3. Run the script:
    ```bash
    python sc

## Troubleshooting

- Error 403: Forbidden: Check with Geoplace to ensure your API account is correctly set up.
- SSL Error: "error:ssl.SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1020)" - Check with your IT team to ensure the Geoplace API is not restricted via firewall, etc.
- SSL/TLS Error: "ssl.SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1020)" - This is related to TLS authentication. Check with your IT team if TLS is enabled, and/or ensure your TLS and SSL versions for Python are up to date.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
- Fork the repository.
- Create your feature branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.

## Acknowledgements
Geoplace DataVIA API documentation

## Contact
For any questions or suggestions, please open an issue or contact me at kevin.ferguson@durham.gov.uk or kevinferguson@hotmail.co.uk
