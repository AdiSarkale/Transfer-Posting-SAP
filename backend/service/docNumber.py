import re

def DocumentNumber(session):
    status_bar_text = session.findById("wnd[0]/sbar").Text
    # words = status_bar_text.split()

    match = re.search(r"\b\d{10}\b", status_bar_text)
    if match:
        return match.group()

    status_bar_text
