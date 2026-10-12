#!/usr/bin/env python3
"""Package only the verified, standalone reader for GitHub Pages downloads."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
from paper_watch import ROOT, build


def package(root=ROOT):
    build(root, check=True)
    output = root / 'dist/research-paper-watch.zip'
    info = ZipInfo('index.html', date_time=(2026, 1, 1, 0, 0, 0))
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    with ZipFile(output, 'w') as archive:
        archive.writestr(info, (root / 'dist/index.html').read_bytes())
    return output


if __name__ == '__main__':
    print(package())
