"""Safety check for the Render 3D Library.

Run from the repository root before every commit:
    python3 -I Tools/SafetyCheck.py

It fails (exit code 1) if any file is not a plain 3D model, texture, text file or
JSON catalogue, if a model points outside its own folder or to the internet, if a
file is executable, or if a file is larger than 30 MB.
"""
import json, os, re, struct, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_BYTES = 30 * 1024 * 1024
ALLOWED = {'.glb', '.gltf', '.bin', '.png', '.jpg', '.jpeg', '.txt', '.md', '.json'}
TOOLS_ALLOWED = {'.py'}
SUSPICIOUS = re.compile(rb'<script|javascript:|powershell|cmd\.exe|/bin/sh|\beval\(|\bexec\(|MZ\x90\x00', re.I)
problems, counts = [], {}


def bad(path, why):
    problems.append(f'{os.path.relpath(path, ROOT)}: {why}')


def check_uris(path, doc):
    folder = os.path.dirname(path)
    for key in ('buffers', 'images'):
        for item in doc.get(key, []):
            uri = item.get('uri')
            if uri is None:
                continue
            if uri.startswith('data:'):
                if not re.match(r'data:(application/octet-stream|application/gltf-buffer|image/png|image/jpeg);base64,', uri):
                    bad(path, f'unexpected embedded data type in {key}')
                continue
            if re.match(r'^[a-z][a-z0-9+.-]*:', uri, re.I) or uri.startswith('/') or '..' in uri.replace('\\', '/').split('/'):
                bad(path, f'{key} uri points outside its folder: {uri[:80]}')
                continue
            from urllib.parse import unquote
            if not os.path.isfile(os.path.join(folder, unquote(uri))):
                bad(path, f'{key} file missing: {uri}')


for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != '.git']
    for name in filenames:
        path = os.path.join(dirpath, name)
        rel = os.path.relpath(path, ROOT)
        ext = os.path.splitext(name)[1].lower()
        in_tools = rel.split(os.sep)[0] == 'Tools'
        counts[ext] = counts.get(ext, 0) + 1
        if os.path.islink(path):
            bad(path, 'symbolic link'); continue
        if ext not in ALLOWED and not (in_tools and ext in TOOLS_ALLOWED):
            bad(path, 'file type not allowed'); continue
        if os.stat(path).st_mode & 0o111:
            bad(path, 'marked as executable')
        if os.path.getsize(path) > MAX_BYTES:
            bad(path, 'larger than 30 MB')
        with open(path, 'rb') as f:
            data = f.read()
        if ext == '.glb':
            if data[:4] != b'glTF' or len(data) < 20:
                bad(path, 'not a real glb file'); continue
            jlen, jtype = struct.unpack('<II', data[12:20])
            if jtype != 0x4E4F534A:
                bad(path, 'glb has no JSON chunk'); continue
            try:
                doc = json.loads(data[20:20 + jlen].rstrip(b' \x00'))
            except Exception:
                bad(path, 'glb JSON unreadable'); continue
            check_uris(path, doc)
            if SUSPICIOUS.search(data[20:20 + jlen]):
                bad(path, 'suspicious text inside model')
        elif ext == '.gltf':
            try:
                doc = json.loads(data)
            except Exception:
                bad(path, 'gltf JSON unreadable'); continue
            check_uris(path, doc)
            if SUSPICIOUS.search(data):
                bad(path, 'suspicious text inside model')
        elif ext == '.png' and data[:8] != b'\x89PNG\r\n\x1a\n':
            bad(path, 'not a real PNG image')
        elif ext in ('.jpg', '.jpeg') and data[:3] != b'\xff\xd8\xff':
            bad(path, 'not a real JPEG image')
        elif ext == '.json':
            try:
                json.loads(data.decode('utf-8'))
            except Exception:
                bad(path, 'JSON file is not plain readable JSON')
            if SUSPICIOUS.search(data):
                bad(path, 'suspicious text')
        elif ext in ('.txt', '.md') and not in_tools:
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                bad(path, 'text file is not plain text')
            if SUSPICIOUS.search(data):
                bad(path, 'suspicious text')
        elif ext == '.bin' and data[:2] == b'MZ':
            bad(path, 'binary looks like a Windows program')

print('Files checked by type:', dict(sorted(counts.items())))
if problems:
    print(f'FAILED: {len(problems)} problem(s)')
    for p in problems:
        print(' ', p)
    sys.exit(1)
print('PASSED: every file is a plain model, texture, text file or JSON catalogue, with no links outside its folder.')
