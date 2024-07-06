# Tip: For faster development, put large, unlikely to change operations first
# This only affects docker build times, not the final app

# Base Docker image form https://hub.docker.com/_/python
FROM python:3.10

# Set the working directory
WORKDIR /home/biolib

# Copy requirements and install them
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy example input data
COPY sample.fasta .

# Copy predict script last (most likely file to change during development)
COPY predict.py .

# We recommend not setting an ENTRYPOINT, as .biolib/config.yml specifies this anyway
# (this makes it easier to develop the container interactively with docker run -it NAME or dev.sh)
# ENTRYPOINT ["python3", "predict.py"]
