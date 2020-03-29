import security
import pytest
from io import StringIO

s = security.Security()

# Caesar Cipher
def test_CaesarEncrypt_1(monkeypatch):
    strinput = StringIO("4\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert type(s.CaesarEncrypt("string")) == str

def test_CaesarEncrypt_2(monkeypatch):
    test_string = "Bingo"
    strinput = StringIO("4\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert s.CaesarEncrypt(test_string) != test_string

def test_CaesarDecrypt_1(monkeypatch):
    strinput = StringIO("4\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert type(s.CaesarDecrypt("string")) == str

def test_CaesarDecrypt_2(monkeypatch):
    test_string = "Bingo"
    strinput = StringIO("4\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert s.CaesarDecrypt(test_string) != test_string

# Polyalphabetic
def test_PolyEncrypt_1(monkeypatch):
    strinput = StringIO("sonic\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert type(s.PolyEncrypt("string")) == str

def test_PolyEncrypt_2(monkeypatch):
    test_string = "Bingo"
    strinput = StringIO("sonic\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert s.PolyEncrypt(test_string) != test_string

def test_PolyDecrypt_1(monkeypatch):
    strinput = StringIO("sonic\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert type(s.PolyDecrypt("string")) == str

def test_PolyDecrypt_2(monkeypatch):
    test_string = "Bingo"
    strinput = StringIO("sonic\n")
    monkeypatch.setattr("sys.stdin", strinput)
    assert s.PolyDecrypt(test_string) != test_string
