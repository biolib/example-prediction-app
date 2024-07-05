#!/bin/bash
# File to run Docker container with mounted files!

# Mount data folder to /data
docker buildx build --platform linux/amd64 -t prediction-app .

# Run interactively, starting a terminal
docker run --rm -it \
    -v $(pwd)/predict.py:/home/biolib/predict.py \
    -v $(pwd)/data/:/home/biolib/data/ \
    prediction-app /bin/bash