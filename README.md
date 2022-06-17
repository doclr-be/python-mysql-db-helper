# MySQL DB Helper
MySQL DB Helper is a Python package that contains handy functions for querying MySQL. 

## Installation and updating
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MySQL DB Helper like below. 
Rerun this command to check for and install  updates .
```bash
pip install git+https://github.com/doclr-be/python-mysql-db-helper
```

## Usage

#### Features:
* DbClient.query  --> returns DbQueryResult that contains rows and headers
* DbClient.query_to_csv --> returns a csv in string format, first row contains headers

#### Demo of some of the features:
```python
from mysql_db_helper import DbClient

host="localhost"
database="students"
port=3306
user="foo"
password="bar"

db_client = DbClient(host,database,port,user,password)
query_result = db_client.query("select * from students")

print(query_result.headers[1]) # => "name"
print(query_result.rows[0][1]) # => "Niels"
```


## License
[MIT](https://choosealicense.com/licenses/mit/)

## References
Project structure based on [Toolbox tutorial](https://github.com/mike-huls/toolbox)
