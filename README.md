# sf-edu-gh-actions

Practice for GitHub Actions.

## About the project

This is a repository for practising GitHub Actions and CI/ID for python projects.

## Developing

### Poetry

To work with this project start with installing Poetry and then run:

    poetry install

After that app will be available on `localhost:9090`

- Swagger UI at `localhost:9090/docs/`

### To run an app:

    poetry run uvicorn app.main:app --reload --host localhost --port 9090

### To run tests:

    poetry run pytest .

### To run format:

    poetry run black .