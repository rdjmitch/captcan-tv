#!/usr/bin/env python3
"""CaptCan TV: serves this folder to the shop network so the store TV plays the channel
from the Mac mini instead of the internet. Supports seeking in video (Range requests)."""
import os, re, sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
PORT = 8788
ROOT = os.path.dirname(os.path.abspath(__file__))

class H(SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a): pass
    def end_headers(self):
        p = self.path.split("?")[0]
        if p.endswith((".html", ".json", "/")):
            self.send_header("Cache-Control", "no-store")
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()
    def send_head(self):
        path = self.translate_path(self.path)
        rng = self.headers.get("Range")
        if not rng or os.path.isdir(path) or not os.path.isfile(path):
            return super().send_head()
        m = re.match(r"bytes=(\d*)-(\d*)$", rng.strip())
        size = os.path.getsize(path)
        if not m or (not m.group(1) and not m.group(2)):
            return super().send_head()
        if m.group(1):
            start = int(m.group(1)); end = int(m.group(2)) if m.group(2) else size - 1
        else:
            start = max(0, size - int(m.group(2))); end = size - 1
        end = min(end, size - 1)
        if start > end:
            self.send_error(416); return None
        f = open(path, "rb"); f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", "bytes %d-%d/%d" % (start, end, size))
        self.send_header("Content-Length", str(end - start + 1))
        self.end_headers()
        self._left = end - start + 1
        return f
    def copyfile(self, src, out):
        left = getattr(self, "_left", None)
        if left is None:
            return super().copyfile(src, out)
        self._left = None
        while left > 0:
            b = src.read(min(65536, left))
            if not b: break
            out.write(b); left -= len(b)

if __name__ == "__main__":
    os.chdir(ROOT)
    try:
        ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
    except OSError as e:
        sys.exit("CaptCan TV server could not start: %s" % e)
