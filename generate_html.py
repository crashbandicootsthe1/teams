# generate_html.py

# Define the content you want to include in the HTML page
page_title = "My Generated HTML Page"
page_content = """
<h1>Welcome to My Generated HTML Page</h1>
<p>This is a basic example of generating HTML content using a Python script.</p>
<p>You can customize this content as needed.</p>
"""

# Create the HTML file
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{page_title}</title>
</head>
<body>
    {page_content}
</body>
</html>
"""

# Write the HTML content to a file (e.g., generated.html)
with open("index.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
