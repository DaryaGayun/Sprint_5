import random
import string

def generate_unique_email():
    return f"user_{random.randint(10000, 99999)}@test.ru"

def generate_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_name(length=6):
    return ''.join(random.choices(string.ascii_letters, k=length))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
