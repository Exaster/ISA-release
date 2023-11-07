import webbrowser

# Open current path
repo_path = "path/to/your/repository"


# Start a local web server, default port 8000
try:
    subprocess.run(["python", "-m", "http.server"], cwd=repo_path)
except Exception as e:
    print(f"Error starting the local web server: {e}")

# Open a browser with the website
webbrowser.open("http://localhost:8000")
