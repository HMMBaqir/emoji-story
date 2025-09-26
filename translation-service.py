import demoji

def convert_emojis_to_text(input_string: str) -> str:
    x = demoji.replace_with_desc(input_string, sep='')
    return x
if __name__ == "__main__":
    test_string = "🌍,🚀"
    converted_string = convert_emojis_to_text(test_string)
    print(converted_string)