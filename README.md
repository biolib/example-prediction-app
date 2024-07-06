Everything you need to deploy this example app is available here: https://github.com/biolib/example-prediction-app

## How to deploy an app on Biolib.com

Every time you run an app on Biolib.com, we spin up a Docker container containing the app on our servers. This container contains the exact program and environment you've specified as a developer, making the app highly reproducible. And infinitely scaleable!

So, how do you deploy an app on Biolib.com?

#### Step 0: Create your [prediction app](https://github.com/biolib/example-prediction-app/blob/main/predict.py) (this one counts Alanines in a FASTA file)

```bash
# Download this example repository
git clone https://github.com/biolib/example-prediction-app
cd example-prediction-app

# Install requirements
pip install -r requirements.txt

# Test that the app works!
python --fasta sample.fasta --outfile predictions.fasta
```

#### Step 1: Create your [Dockerfile](https://github.com/biolib/example-prediction-app/blob/main/Dockerfile), build and test it

```bash
# (We've already done this - but you can use 'docker init' in the future)
cat Dockerfile

# Build image from Dockerfile in this directory, with tag "prediction-app"
docker build . --platform linux/amd64 -t prediction-app

# Run the image as a container, and start a shell within it
docker run -it prediction-app /bin/bash

# Now test your app inside the container!
python predict.py --fasta sample.fasta --outfile predictions.fasta
```

#### Step 2: Create your [.biolib/config.yml](https://github.com/biolib/example-prediction-app/blob/main/.biolib/config.yml) file, and deploy our image on Biolib.com

```bash
# (We've already done this - but you can use 'biolib init' in the future)
cat .biolib/config.yml

# Next we create a new app on Biolib.com
https://biolib.com/new/

# I've used the name prediction-app, found here:
https://biolib.com/BioLibDevelopment/prediction-app

# Before we push, we need to setup an API token (so Biolib knows who we are)
https://biolib.com/settings/api-tokens/

# Set it as an environment variable
export BIOLIB_TOKEN=[your_api_token]

# Everything OK? Let's push the app!
biolib push BioLibDevelopment/prediction-app

# Now check it out on Biolib.com!
https://biolib.com/BioLibDevelopment/prediction-app/
```
## Overview of files
```markdown'
├── README.md               # This file
├── Dockerfile              # How we build the Docker image (everything you need, code-wise)
├── .biolib
│   └── config.yml          # How Biolib interacts with the image 
├── predict.py              # Prediction script
├── sample.fasta            # Example input file
├── predictions.csv         # Example output file
├── requirements.txt        # Dependencies (installed with pip)
├── LICENSE                 # Optional, app license
```

## More Biolib app documentation
- Building applications guide: https://biolib.com/docs/building-applications/intro/
- .biolig/config.yml guide: https://biolib.com/docs/building-applications/syntax-of-config-yml/
- Dockerfile documentation: https://docs.docker.com/reference/dockerfile/
- How does Docker work? https://www.youtube.com/watch?app=desktop&v=IxzwNa-xuIo

## Best development practices
Docker tips:
- Dockerfile: Start with "slow" things, and put files you're likely to change last. Docker caches your build in layers, making quick script changes very quick to rebuild if they're in the last layers.
- Dockerfile: Often using base images like 'ubuntu:22.04' (CPU) or 'nvidia/cuda:12.0.0-devel-ubuntu22.04' is easiest for development. Biolib automatically caches commonly used images for faster loading. If you REALLY care about speed, try using 'alpine:latest'
- Use 'bash [dev.sh](https://github.com/biolib/example-prediction-app/blob/main/dev.sh)' to run the Docker image with an interactive terminal, and bind mount files inside the container (edit files inside/outside - super useful!)

Biolib tips:
- .biolig/config.yml - Create a nice app user-interface with these arguments: https://biolib.com/docs/building-applications/syntax-of-config-yml/#arguments
- .biolig/config.yml - Use 'main_output_file' to get nicer output visualizations (for CSV, FASTA, markdown and text files)
- You can acess your live Biolib app directly from Python. See API examples here: https://biolib.com/docs/using-applications/python/
- Suffering from slow Docker build times? Automatically build on our servers every time you git push with our Biolib Pro subscription. Simply modify this file [.github/workflows/ci.yml](https://github.com/biolibtech/app-musite/blob/develop/.github/workflows/ci.yml) and put it in your .github/workflows directory.

## FAQ

**Why use Docker?**
- Docker solves the problem of "but it runs on my machine!". A Docker image can run on any machine (supporting Docker), can easily be scaled to 1.000 instances, and has an exact, reproducible environment now and 20 years in the future.

**What exactly does pybiolib do?**
- For our purposes, it finds the Docker image you built (from the tag you specified in .biolig/config.yml) and pushes it to Biolib. It also pushes a few other specific files, if they are present, including LICENSE, README, images in README, and of course, the .biolib/config.yml file).

**It doesn't work!**
- Please ask for help in our Biolib community [biolibcommunity.slack.com](https://biolibcommunity.slack.com/), and we are more than happy to help!
