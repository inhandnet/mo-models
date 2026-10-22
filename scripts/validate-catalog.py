#!/usr/bin/env python3
"""Validate models.json and the per-model .link files without network access."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r'^https://[a-z0-9.-]+/[^\s]+$')
REQUIRED = ('id', 'task', 'runtime', 'input', 'boards', 'images', 'tidl', 'source', 'artifact', 'verification')
VERIFICATION = {'inventory', 'audited-latency', 'tutorial'}
errors = []
catalog = json.loads((ROOT / 'models.json').read_text(encoding='utf-8'))
models = catalog.get('models')
if not isinstance(models, list):
    sys.exit('models.json needs a "models" list')
seen = set()
for m in models:
    mid = m.get('id', '?')
    for key in REQUIRED:
        if key not in m:
            errors.append(f'{mid}: missing {key}')
    if mid in seen:
        errors.append(f'{mid}: duplicate id')
    seen.add(mid)
    if m.get('verification') not in VERIFICATION:
        errors.append(f'{mid}: unknown verification {m.get("verification")}')
    d = ROOT / 'models' / mid
    if not (d / 'README.md').is_file():
        errors.append(f'{mid}: models/{mid}/README.md missing')
    for section in ('source', 'upstream_artifact'):
        ref = m.get(section)
        if not ref:
            continue
        link = ROOT / ref['link']
        if not link.is_file():
            errors.append(f'{mid}: {ref["link"]} missing')
            continue
        lines = link.read_text(encoding='utf-8').splitlines()
        if len(lines) != 1 or not URL.match(lines[0]):
            errors.append(f'{mid}: {ref["link"]} must contain exactly one https URL')
        elif lines[0] != ref['url']:
            errors.append(f'{mid}: {ref["link"]} differs from models.json url')
    art = m.get('artifact') or {}
    if art.get('download_url') and art.get('status') == 'pending-hosting':
        errors.append(f'{mid}: pending-hosting entries must not carry a download_url')
    lat = m.get('latency')
    if m.get('verification') == 'audited-latency':
        if not lat or not (ROOT / lat['record']).is_file():
            errors.append(f'{mid}: audited-latency needs an existing latency.record')
    elif lat:
        errors.append(f'{mid}: latency given without audited-latency verification')
for path in (ROOT / 'models').iterdir():
    if path.is_dir() and path.name not in seen:
        errors.append(f'models/{path.name}: directory without models.json entry')
for suffix in ('.onnx', '.tflite', '.bin', '.tar.gz'):
    for path in ROOT.rglob('*' + suffix):
        if '.git' not in path.parts and 'node_modules' not in path.parts:
            errors.append(f'{path.relative_to(ROOT)}: model binaries are not stored in this repository')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'models.json: {len(models)} model(s); link files and records consistent')
