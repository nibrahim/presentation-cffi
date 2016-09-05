from leftpad_cffi_api import leftpad

def test_leftpad():
    ip = "python"
    assert leftpad(ip) == ip.rjust(20)

