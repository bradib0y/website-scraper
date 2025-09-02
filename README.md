## Get started with website-scraper

### Prerequisites

- WSL if you are on Windows
- python, virtualenv
- VSCode, Python extensions (Python Debugger will allow debugging in VSCode)

### Activate python virtualenv:

```
source venv/bin/activate
```

### Dependencies outside of python ecosystem (this will work hopefully, I've had some back-and-forths with these)

```
sudo apt-get update

sudo apt-get install -y \
  libgstreamer1.0-0 libgtk-4-1 libgraphene-1.0-0 libxslt1.1 libevent-2.1-7 \
  gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-libav \
  libavif16 libharfbuzz-icu0 libenchant-2-2 libsecret-1-0 libhyphen0 \
  libmanette-0.2-0 libgles2-mesa libgtk-3-0 libgles2-mesa-dev

playwright install
playwright install-deps
```

### 