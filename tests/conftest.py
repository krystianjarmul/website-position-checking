from http.server import HTTPServer, BaseHTTPRequestHandler
from http import HTTPStatus
from threading import Thread

import pytest

TEST_HOST = "127.0.0.1"
TEST_PORT = 1938
HTML = """
<div id="rso">
    <div class="g">
        <div class="UT76R">
            <h3>Other</h3>
            <a href="https://www.other.com/">other.com</a>
        </div>
    </div>
    <div>
        <span>unnecessarytag</span>
    </div>
    <div class="g">
        <div class="UT76R">
            <h3>Travatar</h3>
            <a href="https://travatar.ai/">travatar.ai</a>
        </div>
    </div>
</div>
"""


class GoogleSearchResultsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(HTML)))
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))


class MockServer:

    def __init__(self, host, port, handler):
        self._server = HTTPServer((host, port), handler)
        self._thread = Thread(target=self._run_thread, daemon=True)

    def _run_thread(self):
        self._server.serve_forever()

    def start(self):
        self._thread.start()

    def stop(self):
        self._server.server_close()
        self._server.shutdown()
        self._thread.join()


@pytest.fixture(scope="module", autouse=True)
def google_mock():
    httpd = MockServer(TEST_HOST, TEST_PORT, GoogleSearchResultsHandler)
    try:
        httpd.start()
        yield
    finally:
        httpd.stop()


@pytest.fixture(scope="function")
def html():
    return HTML
