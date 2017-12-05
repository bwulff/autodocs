#!/bin/bash

# start docker-puller
cd /app && python app.py &

# clone project and checkout target branch
cd /
git clone $PROJECT_GIT_URL project
cd project
git checkout $PROJECT_GIT_BRANCH
cd $PROJECT_MKDOCS_DIR

# start mkdocs server
mkdocs serve --dev-addr 0.0.0.0:8000 --livereload --verbose
