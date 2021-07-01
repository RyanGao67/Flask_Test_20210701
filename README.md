```

(base) ryangao67@ryangao67-ThinkPad-T460s:~/tgao2021$ sudo docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
960cbccaffb85d701d9d6f6c1c5f23039b9eac051ef2134216489eb48c47306e

(base) ryangao67@ryangao67-ThinkPad-T460s:~/tgao2021$ sudo docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                       NAMES
960cbccaffb8   postgres   "docker-entrypoint.s…"   17 seconds ago   Up 16 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   some-postgres

(base) ryangao67@ryangao67-ThinkPad-T460s:~/tgao2021$ sudo docker exec -it 960cbccaffb8 bash
root@960cbccaffb8:/# psql -U postgres
psql (13.3 (Debian 13.3-1.pgdg100+1))
Type "help" for help.

postgres=# CREATE DATABASE mytest;
CREATE DATABASE
postgres=# exit
root@960cbccaffb8:/# exit
exit

(base) ryangao67@ryangao67-ThinkPad-T460s:~/tgao2021$ psql -h localhost -p 5432 -U postgres
Password for user postgres: 
psql (12.7 (Ubuntu 12.7-0ubuntu0.20.04.1), server 13.3 (Debian 13.3-1.pgdg100+1))

WARNING: psql major version 12, server major version 13.
         Some psql features might not work.
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 mytest    | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)

postgres=# \c mytest;
psql (12.7 (Ubuntu 12.7-0ubuntu0.20.04.1), server 13.3 (Debian 13.3-1.pgdg100+1))
WARNING: psql major version 12, server major version 13.
         Some psql features might not work.
You are now connected to database "mytest" as user "postgres".
mytest=# \d

```


### Test

```
curl --header "Content-Type: application/json"   --request POST  --data '{"username":"user5","password":"password5"}'   http://localhost:5000/user
curl --header "Content-Type: application/json"   --request PUT   --data '{"username":"user5","password":"password7"}'   http://localhost:5000/user
curl --request DELETE http://localhost:5000/user/user5
```


### Dependency
```
 conda list -e > requirements.txt
```