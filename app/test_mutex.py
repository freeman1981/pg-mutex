import os
from multiprocessing import Pool

import psycopg2
import pytest

from mutex import generate_lock_id, mutex


def connect():
    return psycopg2.connect(os.getenv('DSN'))


def execute(sql):
    with connect() as cn,  cn.cursor() as c:
        c.execute(sql)
    return c


def worker(_):
    c = execute('SELECT FROM test WHERE test=42 LIMIT 1')
    if not c.rowcount:
        execute('INSERT INTO test(test) VALUES (42)')


def worker_mutex(_):
    with mutex(connect(), ['foo']):
        worker(_)


@pytest.mark.parametrize('one_row, func', [
    (False, worker),
    (True, worker_mutex),
])
def test_mutex(one_row, func):
    execute('CREATE TABLE IF NOT EXISTS test (test integer)')
    execute('TRUNCATE TABLE test')

    with Pool(10) as p:
        p.map(func, range(10))

    c = execute('SELECT * FROM test WHERE test=42')
    assert (c.rowcount == 1) == one_row


def test_mutex_no_wait():
    with pytest.raises(Warning):
        with mutex(connect(), ['foo']), mutex(connect(), ['foo'], wait=False):
            pass


@pytest.mark.parametrize('param, expected', [
    ('123', -2008521774),
    ('1 23', 54408031),
])
def test_generate_lock_id(param: str, expected: int):
    assert generate_lock_id(param) == expected
