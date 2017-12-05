# autodocs 

This image autoamtically clones a configured Git repo, builds its documentation with mkdocs and serves the documentation via HTTP. Update of the source code from the Git repository and re-build of the documentation can be triggered via a web-hook (e.g. configured when code is pushed to GitHub/BitBucket).

Introduction
============

...

Deployment
==========

Environment variables:
- *GIT_REPO_URL* URL of the Git repository to use
- *UPDATE_TOKEN* token for vaidating the web-hook call
