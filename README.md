# BookSwap Console

## Description

BookSwap Console is a command line interface (CLI) application written in Python. It uses the `cmd` module for its core functionality. The application is designed to interact with a set of classes, currently only `BaseModel`, but it can be easily extended to support more classes.

## Features

- Interactive command line interface
- Support for EOF (End of File) command to exit the console
- Handles empty input lines

## Installation

Clone the repository:

```bash
git clone https://github.com/your-repo/bookswap-console.git
cd bookswap-console

## Running the Application
```bash
git clone https://github.com/your-repo/bookswap-console.git
cd BookSwap
### Application
```bash
gunicorn --timeout 120 -b 127.0.0.1:5000 web_dynamic.bookswap:app

### Api
```bash
gunicorn -b 127.0.0.1:5001 api.v1.app:app