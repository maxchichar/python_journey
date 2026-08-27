def parse_nigerian_number(input_string):
    """Convert a Nigerian-style number string to a float."""
    # Remove commas (used as thousand separators)
    cleaned = input_string.replace(",", "")
    # Remove currency symbols
    cleaned = cleaned.replace("₦", "")
    # Remove extra whitespace
    cleaned = cleaned.strip()
    #convert to float
    try:
        return float(cleaned)
    except ValueError:
        cleaned = cleaned.replace(" ", "")
        return float(cleaned)

print(parse_nigerian_number(" ₦2,500.00 "))