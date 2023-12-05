# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Proc Doc",
    version="1.0",
    description="Script para la automatizacion de documentos",
    author="autor",
    author_email="nicolas@procdoc.com",
    url="procdoc.com",
    license="free",
    scripts=["doc_main.py"],
    console=["doc_main.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)

# TODO 
# .\setup.py py2exe