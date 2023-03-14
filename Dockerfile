FROM python3.8
COPY model.pickle .
COPY predict.py .
COPY requirements.txt .
RUN pip3 install -r requirements.txt
