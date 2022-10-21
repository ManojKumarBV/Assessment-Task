FROM python:3.10

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update \
     && apt install -y libgl1 \ 
     && apt install -y libtesseract-dev \ 
     && apt install -y tesseract-ocr

COPY . .

EXPOSE 4000
CMD ["python","app.py","runserver","0.0.0.0:4000"]