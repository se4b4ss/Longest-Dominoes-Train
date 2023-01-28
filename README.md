# Longest Dominoes Train
<br />
This Python code outputs the longest "train" given a set of dominoes and a starting number/pip/target. Each successive longest train is output including same length trains.<br />
<br />
Given this data (manually entered in the code):<br />
initialTarget = 4<br />
dominoes = [(4, 1), (1, 3), (1, 5), (3, 3), (5, 5), (3, 5)]<br />
<br />
This is the output:<br />
[(4, 1), (1, 3)]<br />
[(4, 1), (1, 3), (3, 3)]<br />
[(4, 1), (1, 3), (3, 3), (3, 5), (5, 1)]<br />
[(4, 1), (1, 3), (3, 3), (3, 5), (5, 5), (5, 1)]<br />
[(4, 1), (1, 5), (5, 5), (5, 3), (3, 3), (3, 1)]<br />
Execution time in seconds: 0.0006608963012695312<br />
