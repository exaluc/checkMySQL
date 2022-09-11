# checkMySQL
> Check MySQL connection

Python3

## usage

OS X, Linux or Windows:

```sh
pip install -r requirements.txt
```

pip package:

```sh
pip install checkmysql
```

client:

```sh
checkmysql localhost root password sys 3306
┏━━━━━━━━━━━━━━━━━━━━━━━┓
┃ MySQL test connection ┃
┡━━━━━━━━━━━━━━━━━━━━━━━┩
│ host: localhost       │
│ port: 3306            │
│ state: OK             │
└───────────────────────┘

checkmysql --help
Usage: checkmysql [OPTIONS] [HOST] [USER] [PASSWORD] [DB] [PORT]
```


Python Class:

```python
from checkmysql.connector import MySQLConn

con = MySQLConn.create('192.168.0.1', 'root', 'root_password', 'database_name', 3306)
res = con.fetch("select 1 as checkin;")

if res[0].get('checkin', None) == 1:
    print('db check ok')
else:
    print('db check ko')
```


## Requirements

* Typer
* rich
* PyMySQL

## Meta

Lucian – [@odgon](https://twitter.com/odgon)

Distributed under the MIT license. See ``LICENSE`` for more information.

[checkMySQL](https://github.com/odgon/checkMySQL)