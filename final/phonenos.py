import phonenumbers
from opencage.geocoder import OpenCage

def get_location_and_carrier(number):
  """Parses a phone number, extracts location (if available), and determines carrier.

  Args:
      number: The phone number to extract information from (including country code).

  Returns:
      A dictionary containing 'location' (string) and 'carrier' (string) information,
      or None if either cannot be determined.
  """

  try:
    # Parse the phone number
    parsed_number = phonenumbers.parse(number)

    # Get location (if available)
    geocoder = OpenCage(api_key="4f8a662d018546adb101960033607c02")
    results = geocoder.geocode(number)
    location = None
    if results:
      # Extract the first result's formatted address (may not be precise)
      location = results[0]["formatted"]

    # Determine carrier
    carrier = phonenumbers.carrier.name_for_number(parsed_number, "en")

    return {"location": location, "carrier": carrier}
  except phonenumbers.NumberParseException:
    print("Invalid phone number format.")
    return None

# Example usage
phone_number = "+1234567890"  # Replace with actual phone number
info = get_location_and_carrier(phone_number)

if info:
  print(f"Location: {info['location']}")
  print(f"Carrier: {info['carrier']}")
else:
  print("Could not determine location or carrier.")