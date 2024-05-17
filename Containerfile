FROM docker.io/library/python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .streamlit/ .streamlit/

COPY pages/ pages/

COPY 1_Dashboard.py 1_Dashboard.py

EXPOSE 8501

CMD ["streamlit", "run", "1_Dashboard.py"]
