FROM python:latest
EXPOSE 3000
RUN pip3 install  fastapi[all]
RUN pip3 install  uvicorn
WORKDIR app
COPY . .
CMD  uvicorn app:app  --host 0.0.0.0 --port 3000

