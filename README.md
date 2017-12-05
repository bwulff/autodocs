# autodocs 

This image autoamtically clones a configured Git repo, builds its documentation with mkdocs and serves the documentation via HTTP. Update of the source code from the Git repository and re-build of the documentation can be triggered via a web-hook (e.g. when code is pushed to GitHub or BitBucket).

## Deployment

Environment variables:
- **PROJECT_GIT_URL**: the URL of the Git repository to use
- **PROJECT_GIT_BRANCH**: branch to checkout after repo was cloned
- **PROJECT_MKDOCS_DIR**: directory in which the `mkdocs.yml` file is located

Container ports:
- **8000**: mkdocs server
- **8001**: web hook server

**Example:**
```
docker run --rm --name autodocs -p 8000:8000 -p 8001:8001 -e "PROJECT_GIT_URL=https://github.com/bwulff/autodocs-test.git" -e "PROJECT_GIT_BRANCH=master" -e "PROJECT_MKDOCS_DIR=." autodocs
```
You can trigger the update hook with a POST to the `/update` method with a valid token as parameter:
```
curl -X POST http://localhost:8001/update?token=test123
```
