### Data Sets

[Year 2001 Flight Delays](https://drive.google.com/file/d/0Bylu3dRYpIlXeGIyWGpKUUFKWEk/view?usp=sharing)

[U.S. Life Expectancies](https://raw.githubusercontent.com/vicapow/angular-d3-talk/master/slides/demos/life-expectancy/life-expectancy-by-sex-race-and-state.csv)

[Worldwide Life Expectancies, Populations, Incomes](https://drive.google.com/file/d/0Bylu3dRYpIlXS0xQaENzUEg5dnc/view?usp=sharing)

[The Complete Works of Shakespeare - Compute Word Count](https://drive.google.com/file/d/0Bylu3dRYpIlXZXVRcjlQN2gzeHM/view?usp=sharing)

[The Brown Corpus (NLTK) - Genre Classification with Cosine Similarity](https://github.com/dserban/pyspark2015summer/blob/master/brown.md)

[Million Song Subset](http://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset#subset)

[AudioScrobbler](http://www-etud.iro.umontreal.ca/~bergstrj/audioscrobbler_data.html)

[Titanic Survival Data Set](http://lib.stat.cmu.edu/S/Harrell/data/ascii/titanic.txt)

[Detect Regional and Global Peak Oil Events](https://gist.github.com/dserban/fa1c41affb4fee0d24ea)

[USA 2011 Car Crash Data](https://drive.google.com/file/d/0Bylu3dRYpIlXRDdKeVBmbzFkYlE/view?usp=sharing)

[Sentiment-Labeled Sentences](http://archive.ics.uci.edu/ml/machine-learning-databases/00331/)

[MovieLens - Build a Recommender System](https://github.com/Blosc/movielens-bench/tree/master/ml-10m)

[Twitter Stream - Detect Sentiment](https://drive.google.com/file/d/0Bylu3dRYpIlXLWRSSDA4R2VBUGc/view?usp=sharing)

[Randomly Generated People Data](https://drive.google.com/file/d/0Bylu3dRYpIlXY0dPdUJKS3dwN3M/view?usp=sharing)

[Graph Data - Apply PageRank to it](https://drive.google.com/file/d/0Bylu3dRYpIlXUDdjU2VweTE2MVU/view?usp=sharing)

[StackExchange Data Dump (11GB)](https://archive.org/details/stackexchange)

[Reddit Comments Data Dump](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/)

[bank.csv](https://s3.amazonaws.com/apache-zeppelin/tutorial/bank/bank.csv)

**Electrocardiograms:**  
[What the data looks like](http://dserban.github.io/physiobank/chart.html)  
Where to get the data:
```
wget http://www.physionet.org/physiobank/database/mitdb/100.dat
wget http://www.physionet.org/physiobank/database/mitdb/100.hea
```

[Extract data from the NationStates API and run analytics on it](https://www.nationstates.net/pages/api.html)

### Data Locality

[Data Partitioning Explained](https://www.safaribooksonline.com/library/view/learning-spark/9781449359034/ch04.html)

**Bad Data Locality:**
```
 (1,'a')   (1,'m')
 (1,'b')   (2,'n')
_________ _________

 (1,'c')   (3,'o')
 (2,'d')   (3,'p')
_________ _________

 (2,'e')   (3,'q')
 (2,'f')   (4,'r')
_________ _________

 (3,'g')   (4,'s')
 (4,'h')   (4,'t')
```

**Good Data Locality:**
```
 (1,'a')   (1,'m')
 (1,'b')
 (1,'c')
_________ _________

 (2,'d')   (2,'n')
 (2,'e')
 (2,'f')
_________ _________

 (3,'g')   (3,'o')
           (3,'p')
           (3,'q')
_________ _________

 (4,'h')   (4,'r')
           (4,'s')
           (4,'t')
```
