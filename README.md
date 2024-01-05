# Bryan Chasko's Flask Website 🌟

This project is a website built using Flask, Python, HTML templates, and AWS S3 for deployment. The intent is to utilize as much python as possible throughout the website.

## Next Steps - Routing & setting up custom domain with route53

## Table of Contents 📜

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Structure 📂

The main directories and files include:

- `app.py`: Flask application setup and routing
- `templates/`: HTML templates for different sections
- `build/`: Directory containing the built HTML files
- `README.md`: Project overview and instructions (you're reading it!)

## Installation 🚀

1. Clone the repository.
2. Set up a virtual environment: `python3 -m venv foo_venv`.
    i.e., `python3 -m venv flask_bryanchasko_venv`
3. Activate the virtual environment: `source foo_venv/bin/activate` 
    i.e., `source flask_bryanchasko_venv/bin/activate`
    when done with your virtual environment session run `deactivate`
4. Install the dependencies: `pip install -r requirements.txt`.

## Usage 🖥️

To run the Flask app locally:

```bash
python3 app.py
```

## Build
flask-freeze will create a "build" folder with the built flask project. you're ready to sync the build folder contents to s3.

## Deploy to s3 static website hosting
from your build directory, run:
```bash
aws s3 sync . s3://bryanchaskoflasksite2024/ --delete
```



