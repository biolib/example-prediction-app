# For faster development, do large operations first
# Base Docker image form https://hub.docker.com/_/python
FROM python:3.10

# Set the working directory
WORKDIR /home/biolib

# Copy requirements and install them
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Now run
COPY data/sample.fasta data/sample.fasta
RUN mkdir output/
COPY predict.py .

# Entrypoint (Nb: Will break dev.sh -> use .biolib/config.yml instead
# ENTRYPOINT ["python3", "predict.py"]