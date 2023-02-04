Cornerstone
======

The Pilar's test case to backend


Setup
-------

### Clone the repository

```bash
git clone git@github.com:maikyguanaes/cornerstone.git
cd cornerstone
```

```bash
# checkout the correct version
git fetch --all --tags --prune && git pull origin main --rebase
```

### Create a virtualenv and activate it

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

### Install dependencies
```bash
pip3 install -r requirements_dev.txt
```

#### Copy Env
```bash
cp .env.example .env
```


### Run as CLI
```bash
flask run
# OR
flash shell
```

### Run as Container (Docker Compose)
```bash
docker-compose up
```

Open http://127.0.0.1:8080 in a browser.


### Test
```bash
pytest -vv
# OR
pytest -vv -s -- <file>
# OR
ptw -- -vv -s <file>
```

### Run with coverage report
```bash
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```