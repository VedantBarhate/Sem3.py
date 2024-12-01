import re

def find_emails(input_text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, input_text)
    return emails

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    input_text = "test123@gmail.com & notaemail@@test.com & new@hotmail.com"
    email_list = find_emails(input_text)
    print("Found emails:", email_list)
