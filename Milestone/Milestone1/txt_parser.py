import re

def parse_txt(file):
    text = file.read().decode("utf-8")
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
