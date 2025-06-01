def clear_backticks(text):
    if text.startswith("```"):
        text=text[3:].strip()
    if text.endswith("```"):
        text=text[:-3].strip()
    return text