# PG MUTEX

Python wrapper around Postgres `pg_advisory_lock` and `pg_try_advisory_lock` functions. It is possible, thanks to a common connection to the database, to block certain pieces of python code by different python processes, on different nodes.


### Installation

```shell
pip install pg-mutex
```


### Usage

```python
from mutex import mutex

with mutex(connection, ['param1', 'param2']):
    # here is code that is guaranteed to be executed by only one process, even on different nodes
    pass
```


### Run test

```shell
docker-compose run app wait-for db:5432 -- pytest -x --cov=. test_mutex.py --cov-fail-under 65
```

### Run linter

```shell
docker-compose run app flake8
```
