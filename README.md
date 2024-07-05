Everything you need to deploy this example app is available here:
https://github.com/biolib/example-prediction-app

## Introduction

Everytime you run a job on Biolib.com, a Docker image containing your app is spun up on an AWS server. The docker image contains the exact programs and environment you've specified, making your app highly reproducible and infinitely scaleable.

How do we deploy an app on Biolib.com?

Here is an example with a simple program that calculates the number of Alanines in a FASTA file.

#### Step 1: Create your prediction app, with input and output files
- Example [prediction app](predict.py)

```bash
# Download this repository
git clone https://github.com/biolib/example-prediction-app
cd example-prediction-app

# Install requirements
pip install -r requirements.txt

# Test that the app works!
python --fasta sample.fasta --outfile predictions.fasta
```

#### Step 2: Create a Dockerfile and build its image
- Example Dockerfile: [Dockerfile](Dockerfile)
- Dockerfile documentation: [https://docs.docker.com/reference/dockerfile/](https://docs.docker.com/reference/dockerfile/)

```bash
# We've already made an example Dockerfile
less Dockerfile

# Build image from Dockerfile in this directory, with tag "prediction-app"
docker build . --platform linux/amd64 -t prediction-app

# Run the image as a container, and start a shell within it
docker run -it prediction-app /bin/bash

# Now test your app again!
python predict.py --fasta sample.fasta --outfile predictions.fasta
```

#### Step 3: Everything successful? Let's deploy it on Biolib.com!
- Example [.biolib/config.yml](.biolib/config.yml) file
- Read more: # See https://biolib.com/docs/building-applications/syntax-of-config-yml/

```bash
# First we need to setup a .biolib/config.yml file. We've already done this.
# 
# The .biolib/config.yml file tells our Biolib backend:
# - Where to find the built image (we need the image tag name)
# - What input arguments the app expects, and output file
# - How the web app should look (input arguments etc)
less .biolib/config.yml

# Next we create a new app on Biolib.com
https://biolib.com/new/

# I've used the name test-app, found here:
https://biolib.com/BioLibDevelopment/test-app/

# Before we push, we need to setup an API token (so Biolib knows who we are)
https://biolib.com/settings/api-tokens/

# Set it as an environment variable
export BIOLIB_TOKEN=[your_api_token]

# Everything OK? Let's push the app!
biolib push BioLibDevelopment/prediction-app

# Now check it out on Biolib.com!
https://biolib.com/BioLibDevelopment/prediction-app/
```

## More Biolib app documentation
- This example app: https://github.com/biolib/example-prediction-app
- Building applications guide: https://biolib.com/docs/building-applications/intro/
- config.yml guide: https://biolib.com/docs/building-applications/syntax-of-config-yml/
- Dockerfile documentation: https://docs.docker.com/reference/dockerfile/

## Overview of files
```markdown
├── .biolib
│   └── config.yml          # How Biolib interacts with the image 
├── Dockerfile              # How we build the image (everything you need, code-wise)
├── LICENSE                 # Optional app LICENSE
├── README.md               # What you're reading now
├── data
│   └── sample.fasta        # Example input file
├── output
│   └── predictions.csv     # Example output file
├── predict.py              # Main script
├── requirements.txt        # App environment requirements (pip)
```

## Best development practices
Docker tips:
- Use bash [dev.sh][dev.sh] for an interactive terminal inside the Docker container, including interactively editing your files inside and outside it (using bind mount)
- Put "slow" operations in the beginning of the Dockerfile. Docker will cache your results, making future 'docker build' much faster
- Often using base images like 'ubuntu:22.04' (CPU) or 'nvidia/cuda:12.0.0-devel-ubuntu22.04' is easiest. Biolib automatically caches commonly used images. If you REALLY care about speed, try using 'alpine:latest'

Biolib tips:
- You can modify the interface of your online Biolib app with these .biolib/config.yml arguments: https://biolib.com/docs/building-applications/syntax-of-config-yml/#arguments
- Use the main_output_file argument to automatically get a nice output visualization (recognizes CSV, FASTA, markdown and text files)
- You can also run your Biolib app directly from Python. See examples here: https://biolib.com/docs/using-applications/python/
- As a professional user, we offer fast, automatic building on our Biolib servers, every time you run git push. Simply modify this [.github/workflows/ci.yml](https://github.com/biolibtech/app-musite/blob/develop/.github/workflows/ci.yml) and put it in .github/workflows directory.

## FAQ

Q: Why use Docker?
A: Docker solves the problem of "but it runs on my machine!". A Docker image can run on any machine (supporting Docker), can easily be scaled to 1.000 instances, and has an exact, reproducible environment now and 20 years in the future.

Q: What exactly does pybiolib do?
A: For our purposes, it finds the Docker image you built (from the tag you specified in .biolig/config.yml) and pushes it to Biolib. It also pushes a few other specific files if present (README, images linked to in README, LICENSE, and of course, the config.yml file).

Q: It doesn't work!
A: Please ask for help in our Biolib community (biolibcommunity.slack.com) and we're more than happy to help!