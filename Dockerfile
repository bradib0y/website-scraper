# Use an official Python runtime as a parent image
FROM python:3.12-slim-trixie

# 'BUILD_IMAGE_FOR_DEV' argument and environment variable:
#   we are using this to conditionally use debugpy, a library that allows remote debugging,
#   enabling the VSCode debugger to work inside a container
ARG BUILD_IMAGE_FOR_DEV=false
ENV BUILD_IMAGE_FOR_DEV=$BUILD_IMAGE_FOR_DEV

# Set the working directory in the container
WORKDIR /app

# Install system dependencies required by Playwright and other libraries
# These are based on the `apt-get install` command in README.md
RUN apt-get update && apt-get install -y \
    libgstreamer1.0-0 libgtk-4-1 libgraphene-1.0-0 libxslt1.1 libevent-2.1-7 \
    gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-libav \
    libavif16 libharfbuzz-icu0 libenchant-2-2 libsecret-1-0 libhyphen0 \
    libmanette-0.2-0 libgles2 libgtk-3-0 libgles2-mesa-dev \
    # Clean up APT when done
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install debugpy if BUILD_IMAGE_FOR_DEV is true
RUN if [ "$BUILD_IMAGE_FOR_DEV" = "true" ] ; then pip install debugpy ; fi

# Install Playwright browsers
# This command is from the README.md
RUN playwright install --with-deps

# Copy the application script into the working directory
COPY scrape.py .

# Run the scrape.py script when the container launches
CMD ["python", "scrape.py"]