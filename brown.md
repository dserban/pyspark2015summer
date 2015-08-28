```
>>> from nltk.corpus import brown
>>> brown.words()
[u'The', u'Fulton', u'County', u'Grand', u'Jury', ...]
>>> len( brown.words() )
1161192
>>> brown.categories()
[u'adventure', u'belles_lettres', u'editorial', u'fiction', u'government', u'hobbies', u'humor', u'learned', u'lore', u'mystery', u'news', u'religion', u'reviews', u'romance', u'science_fiction']
>>> brown.words(categories='fiction')
[u'Thirty-three', u'Scotty', u'did', u'not', u'go', ...]
>>> brown.words(categories='romance')
[u'They', u'neither', u'liked', u'nor', u'disliked', ...]
>>> len( brown.words(categories='fiction') )
68488
>>> len( brown.words(categories='romance') )
70022
```
