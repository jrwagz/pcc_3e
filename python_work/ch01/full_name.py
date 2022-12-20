first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)

test_str = "Languages:\n\tPython\n\tC\n\tJavaScript"
print(test_str)

favorite_lanuage = ' python '
print(f"[{favorite_lanuage}]")
print(f"[{favorite_lanuage.rstrip()}]")
print(f"[{favorite_lanuage.lstrip()}]")
print(f"[{favorite_lanuage.strip()}]")

nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))

message = "One of Python's strengths is its diverse community."
print(message)