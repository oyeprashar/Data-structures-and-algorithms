# Notes (move to a directory if this grows)

## Finding shortest distance in matrices between any two indices (some calls can be blocked) using BFS
* Use BFS to count the number of levels needed to reach the destination index
* We will be incrementing the counter after processing a complete level as we want to count that and not the number of nodes encountered before we reach the destination

