## Deploy to fly.io

export FLYCTL_INSTALL="/Users/gerald/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"

fly ssh console -a rezeptothek
Connecting to fdaa:c:5f7f:a7b:60:dde1:bc3e:2... complete

root@2871966b37e7d8:/app# ls
Dockerfile  fly.toml   rdb_neu		 rezepte  templates
db.sqlite3  manage.py  requirements.txt  static

root@2871966b37e7d8:/app# cd ..

root@2871966b37e7d8:/# cd data

root@2871966b37e7d8:/data# ls
db.sqlite3  lost+found

root@2871966b37e7d8:/data# rm db.sqlite3 

root@2871966b37e7d8:/data# ls
lost+found

root@2871966b37e7d8:/data# exit
logout

Geralds-MBP:rezeptdatenbank gerald$ fly sftp shell
» cd data
[/data/]
» put db.sqlite3
180224 bytes written



```
fly deploy -a rezeptothek
```

Connect to fly.io
```
fly ssh console -a rezeptothek
```

Get DB from fly.io
```
fly sftp get /data/db.sqlite3 ./db.sqlite3 -a rezeptothek
```


SFTP
fly sftp shell