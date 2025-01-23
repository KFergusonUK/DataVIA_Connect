import http.client
import base64
import ssl

## UID AND PASSWORD CAN BE HARD CODED, SHOULD YOU BE SO INCLINED.
## USRN_IN CAN BE AMENDED TO RECIEVE INPUT FROM ELSEWHERE.

## SOME OF THE ERRORS I ENCOUNTERED, AND HOW I RESOLVED THEM:
## ERROR 403: FORBIDDEN -- CHECK WITH GEOPLACE YOUR API ACCOUNT IS CORRECTLY SETUP. 
## SSL ERROR: "error:ssl.SSLEOFError: [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol (_ssl.c:1020)" -- CHECK WITH YOUR IT TEAM THE GEOPLACE API IS NOT RESTRICTED VIA FIREWALL, ETC.
## SSL/TLS ERROR: "ssl.SSLError: [SSL: SSLV3_ALERT_HANDSHAKE_FAILURE] sslv3 alert handshake failure (_ssl.c:1020)" -- THIS IS RELATED TO TLS AUTHENTICATION, CHECK WITH YOUR IT TEAM IF TLS IS ENABLED, AND/OR YOUR TLS AND SSL VERSIONS FOR PYTHON ARE UP TO DATE.

#Username and Password input:
USERNAME = input("Please input your username: ")
PASSWORD = input("Please input your password: ")
USRN_IN = input("Which USRN would you like to query?: ")

# Set Base Geoplace API URL:
BASE_URL = 'www.datavia.geoplace.co.uk'


def get_street_data(usrn):
    context = ssl.create_default_context()  # Use default SSL context, for Basic login.
    conn = http.client.HTTPSConnection(BASE_URL, context=context)
    auth = base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
    headers = {
        'Authorization': f'Basic {auth}',
        'Content-Type': 'text/xml'
    }
    
    body = f"""
    <wfs:GetFeature
      service="WFS"
      version="1.1.0"
      outputFormat="geojson"
      xmlns:wfs="http://www.opengis.net/wfs"
      xmlns:gml="http://www.opengis.net/gml"
      xmlns:ogc="http://www.opengis.net/ogc"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.opengis.net/wfs
                          http://schemas.opengis.net/wfs/1.0.0/WFS-basic.xsd">
        <wfs:Query typeName="ms:StreetLines" srsName="EPSG:4326">
            <ogc:Filter>
                <ogc:PropertyIsEqualTo>
                    <ogc:PropertyName>usrn</ogc:PropertyName>
                    <ogc:Literal>{usrn}</ogc:Literal>
                </ogc:PropertyIsEqualTo>
            </ogc:Filter>
        </wfs:Query>
    </wfs:GetFeature>
    """
    
    conn.request("POST", "/api/OgcService/basic/nsg-services-basic", body=body, headers=headers) # Connect to Basic login service url.
    response = conn.getresponse()
    
    if response.status == 200:
        data = response.read()
        return data.decode()
    else:
        return f"Error: {response.status} - {response.reason}"


street_data = get_street_data(USRN_IN) #Function call.
print(street_data) # Display returned result.

