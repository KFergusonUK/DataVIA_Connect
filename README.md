# DataVIA_Connect

This Python script connects to the Geoplace DataVIA API and retrieves street data for a specified USRN (Unique Street Reference Number) using a Basic connection to the Geoplace DataVIA service.

Could be used as a basis for returning USRN details from Geoplace for other projects.

## Features

- Connects to the Geoplace DataVIA API
- Retrieves street data for a given USRN
- Uses Basic authentication for API access

## Requirements

- Python 3.x
- Geoplace DataVIA Account (https://datavia.geoplace.co.uk/)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/KFergusonUK/DataVIA_Connect.git
    ```
2. Navigate to the project directory:
    ```bash
    cd DataVIA_Connect
    ```
Alternatively, download the .py file and double click.

## Usage

1. Gather your Geoplace DataVIA API credentials.
2. Run the script

## Troubleshooting

- Error 403: Forbidden: Check with Geoplace to ensure your API account is correctly set up. Could also be your username and/or password is incorrect.
- SSL Error: "error:ssl.SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1020)" - Check with your IT team to ensure the Geoplace API is not restricted via Proxy/Firewall, etc.
- SSL/TLS Error: "ssl.SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1020)" - This can be related to TLS authentication. Check with your IT team if TLS is enabled on the device you are running the script from, and/or ensure your TLS and SSL versions for Python are up to date.
- Other common API errors and resolutions can be located in the API Documentation here: https://datavia.geoplace.co.uk/documentation

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
- Fork the repository.
- Create your feature branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.

## Acknowledgements
Geoplace DataVIA API documentation, and Support team.

## Contact
- For any questions or suggestions regarding this Python script, please open an issue or contact me at kevin.ferguson@durham.gov.uk or kevinferguson@hotmail.co.uk
- Further information on DataVIA can be found here: https://www.geoplace.co.uk/addresses-streets/street-data-and-services/datavia-api
