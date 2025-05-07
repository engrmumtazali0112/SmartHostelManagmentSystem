# digitalpersona.py - Place this file in the same directory as your views.py

class Device:
    def __init__(self):
        print("Mock DigitalPersona device initialized")
        
    def capture(self):
        print("Mock fingerprint capture - simulating successful capture")
        # Return a consistent mock fingerprint template for testing
        return b"mock_fingerprint_data_123456789"