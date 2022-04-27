# OCR Tesseract Example

Docker container with Flask simple form to upload and OCR an image.

It will "mount" the local directory into the container - any files or changes
you make in the container, will be reflected locally.

## Installing and Running

```
$ docker build -t ocr-tesseract-webapp .
$ docker run -d -p 5000:5000 ocr-tesseract-webapp
```

## Running a command on the container

- `$ docker-compose exec ocr-tesseract-webapp hostname`

## Open a bash terminal on the container

- `$ docker-compose exec ocr-tesseract-webapp /bin/bash`
