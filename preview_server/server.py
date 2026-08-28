"""
Zero-dependency HTTP Preview Server & Live Canvas.
"""

import http.server
import socketserver
import os
import webbrowser
import threading


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, directory=directory or "./output", **kwargs)


def start_preview_server(port: int = 8080, directory: str = "./output", open_browser: bool = True):
    """Starts local server and opens browser."""
    os.makedirs(directory, exist_ok=True)
    handler = lambda *args, **kwargs: CustomHandler(*args, directory=directory, **kwargs)
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        url = f"http://localhost:{port}"
        print(f"🎨 SuperDesign Preview Canvas running at: {url}")
        print(f"📁 Serving artifacts from: {os.path.abspath(directory)}")
        print("Press Ctrl+C to stop the server.")
        if open_browser:
            threading.Timer(0.5, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server stopped.")
