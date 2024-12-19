# novel-translater
novel translater based on 69shu.com


### its kind of working... for example

```python
url = 'https://www.69shu.com/txt/47115/31439983' # books url
dburl = '' # your authentacation key from mongodb
chapter = 50 # how many chapter should be translated
test = database(dburl, url, 50)
test.connectToCollection()
```

## after writing those things in database.py you can run it

and then the content will be safed into your db for future use
