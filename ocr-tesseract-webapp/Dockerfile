FROM python:3.9

RUN apt-get update && apt install -y libsm6 libxext6 python3-opencv
RUN apt -y install tesseract-ocr

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]