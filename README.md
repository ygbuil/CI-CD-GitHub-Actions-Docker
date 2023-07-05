# CI-CD-Github-Actions-Docker

## Description

This project is an implementation of a CI-CD pipeline to deploy a FastAPI backend on a production system using Docker. The project consists of a dummy FastAPI backend and a dummy test (those are irrelevant for the purpose of the project), a CI-CD Pipelines found in `.github/workflows` and some docker files.

**CI Pipeline:** Whenever a push is made to the repo, the CI Pipeline is automatically triggered, following these steps:

* Create a VM with the specified OS.
* Checkout the code in the VM and install the project dependencies.
* Run tests on the VM.

**CD Pipeline:** The CD Pipeline can only be triggered manually, whenever the code wants to be pushed to production. When this pipeline is triggered, it follows these steps:

* Stop Docker container.
* Pull code, install requirements and run tests.
* Start Docker container.

## How to use it

* Clone the repository.
* Go to `Settings` -> `Actions` -> `Runners` and create a runner. Activate the runner on your production server.

On the actions tab of the repository you can see status of the pipelines. To trigger the CI Pipeline, just push some code. To trigger the CD Pipeline go to `Actions` -> `CD Pipeline` -> `Run workflow` -> `Run workflow`.

## Pipelines status

[![CI Pipeline](https://github.com/ygbuil/CI-CD-GitHub-Actions-Docker/actions/workflows/ci_pipeline.yml/badge.svg?branch=master)](https://github.com/ygbuil/CI-CD-GitHub-Actions-Docker/actions/workflows/ci_pipeline.yml)

[![CD Pipeline](https://github.com/ygbuil/CI-CD-GitHub-Actions/actions/workflows/cd_pipeline.yml/badge.svg?branch=master)](https://github.com/ygbuil/CI-CD-GitHub-Actions-Docker/actions/workflows/cd_pipeline.yml)