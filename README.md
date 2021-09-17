# coding-challenges-python-api

## Required tool to run test locally:
- Python 3.8 and above
- Python virtual environment ([how to install](https://virtualenv.pypa.io/en/latest/installation.html))


## Build Setup Steps:
Please go into the repository folder by your favorite command-line app (cmd.exe, bash, etc.)

```bash
# install virtual environment
python -m venv venv

# activate virtual environment (windows)
venv\Scripts\activate

# activate virtual environment (mac/linux)
source venv/bin/activate

# update pip (Python package manager)
python -m pip install --upgrade pip

# install dependencies
pip install -r requirements.txt


# set virtual environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# run application
flask run
```

