# -*- coding: utf-8 -*-
import colorama
from colorama import Fore
import time
import os
from datetime import datetime
from docx import Document
from doc_funcs import * 
from distutils.core import setup
import py2exe

setup(
    name="Proc Doc",
    version="1.0",
    description="Script para la automatizacion de documentos",
    author="autor",
    author_email="nicoarbar@github.com",
    url="procdoc.com",
    license="free",
    scripts=["doc_main.py"],
    console=["doc_main.py"],
    options={"py2exe": {"bundle_files": 1, 'compressed': True}},
    #windows = [{'script': "doc_main.py"}],
    zipfile=None,
)

# .\setup.py py2exe
# pyinstaller doc_main.py