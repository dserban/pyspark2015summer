**PageRank**

The PageRank algorithm aims to assign a measure of importance (called a rank) to each document in a set based on how many documents have links to it. Besides web pages PageRank can also be used to rank scientific articles based on citations, or influential users in a social network based on their followerships.

PageRank proceeds as follows:

- Initialize each page's rank to 1.0.
- On each iteration, have page p send a contribution of rank(p)/numNeighbors(p) to its neighbors (the pages it has links to).
- Set each page’s rank to 0.15 + 0.85 * contributionsReceived.

The last two steps repeat for several iterations, during which the algorithm will converge to the correct PageRank value for each page. In practice, it's typical to run about 10 iterations.

See also [the Pregel paper](http://kowshik.github.io/JPregel/pregel_paper.pdf) and [this blog post](http://googleresearch.blogspot.ro/2009/06/large-scale-graph-computing-at-google.html).
