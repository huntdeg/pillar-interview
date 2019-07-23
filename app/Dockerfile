FROM python:3.7.4
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3261:3261
CMD ["python", "app.py"]
