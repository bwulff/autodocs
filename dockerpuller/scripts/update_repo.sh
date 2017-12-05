#!/bin/bash

echo "Update hook triggered, updating project branch $PROJECT_GIT_BRANCH from $PROJECT_GIT_URL"
cd /project
git pull origin $PROJECT_GIT_BRANCH
