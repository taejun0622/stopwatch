# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path

pyfiglet_path = Path('/Users/taejun/Library/Caches/pypoetry/virtualenvs/stopwatch-1Z_GpYmy-py3.11/lib/python3.11/site-packages/pyfiglet')
fonts_path = pyfiglet_path / 'fonts'

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[(str(fonts_path), 'pyfiglet/fonts')],
    hiddenimports=['pyfiglet.fonts'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='stopwatch',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
