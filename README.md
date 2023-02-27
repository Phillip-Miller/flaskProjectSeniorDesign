# flaskProjectSeniorDesign

To view our rest api documentation:

``` http://127.0.0.1:8000/api/ui/ ```

Internal

To init data base prev flask shell, db.create_all():

```
import sqlite3 conn = sqlite3.connect("user.db")
columns = [ "id INTEGER PRIMARY KEY", "username VARCHAR UNIQUE", "score VARCHAR", "timestamp DATETIME",]
create_table_cmd = f"CREATE TABLE user ({','.join(columns)})"
conn.execute(create_table_cmd)
```

To run local host - could maybe use flask run

``` python app.py```

note need to run to generate the api ui

```pip install "connexion[swagger-ui]"```


