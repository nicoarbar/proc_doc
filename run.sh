#!/bin/bash

if [ "$1" == "push" ]; then
    git add .
    git commit -m "committing from Surface borom"
    git push
else
    streamlit run streamlit_app.py
    #start http://localhost:8501
    #docker build -t streamlit-app .
    #docker run -p 8501:8501 streamlit-app

    #FLASK
    #cd..
    #python flask_app.py
    #start http://localhost:5000
fi