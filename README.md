# scurri-challenge
To launch the api: 
- run app.py
- browse to http://localhost:5000/

Api Sample Usage:
http://localhost:5000/api/v1/validate?postcode=E C1A 1BB

Result:
{
  "format_status": true, 
  "formatted_postcode": "EC1A 1BB", 
  "postcode": "E C1A 1BB", 
  "validation_status": "Valid Postcode"
}
