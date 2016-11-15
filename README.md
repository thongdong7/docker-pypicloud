# Docker Pypicloud

> Docker image for pypicloud


# Usage

Note: See `docker-compose.yml` to know how to config

## Run container

```
docker-compose up
```

See [https://pypicloud.readthedocs.io/en/latest/topics/getting_started.html] for more info

## Install package

```
pip install -i http://localhost:7001/pypi/ PACKAGE1 [PACKAGE2 ...]
```

## Config

If you want to configure pip to always use PyPI Cloud, you can put your preferences into the ``$HOME/.pip/pip.conf` file:

```ini
[global]
index-url = http://localhost:7001/pypi/
```

## Uploading Packages

To upload packages, you will need to add your server as an index server inside your `$HOME/.pypirc`:

```ini
[distutils]
index-servers = pypicloud

[pypicloud]
repository: http://localhost:6543/pypi/
username: <<username>>
password: <<password>>
```

Now to upload a package you should run:

```
python setup.py sdist upload -r pypicloud
```

# Known issues

## Bad gateway

Maybe because of the session. Try to clear browser cache and try again.
