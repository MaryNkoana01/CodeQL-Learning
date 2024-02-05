def generate_html(input_data):
    # Introducing a cross-site scripting (XSS) vulnerability
    return f"<p>{input_data}</p>"

# Simulating untrusted user input
user_input = "<script>alert('This is an XSS vulnerability!');</script>"
html_content = generate_html(user_input)

print("Generated HTML:")
print(html_content)
