import pytest
from app import verify_crsids, santisie_crsid_list

def test_verify_crsid():
    crsids_valid = ["abc123", "def456", "lw664"]
    crsids_invalid = ["abc123\r", "de321"]
    crsids_injection_attempt = ["abc123\n", "def456", "ghi789", "DROP TABLE", "<script>alert('xss')</script>"]
    crsids_capitals = ["ABC123", "DEF456", "LW664"]

    assert verify_crsids(crsids_valid) == True
    assert verify_crsids(crsids_invalid) == False
    assert verify_crsids(crsids_injection_attempt) == False
    assert verify_crsids(crsids_capitals) == True

def test_santisie_crsid_list():
    string1 = "abc123\r\ndef456\nghi789"
    string2 = "111_fjfjru39\nab123"
    string3 = "<script>alert('xss')</script>"

    assert santisie_crsid_list(string1) == ["abc123", "def456", "ghi789"]
    assert santisie_crsid_list(string2) == ["111fjfjru39", "ab123"]
    assert santisie_crsid_list(string3) == ["scriptalertxssscript"]