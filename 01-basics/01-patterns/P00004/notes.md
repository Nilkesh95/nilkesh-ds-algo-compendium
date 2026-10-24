
## Approach

Here we see that:<br>
when i=0, j is 0,        but 1     is printed<br>
when i=1, j is 0,1       but 22    is printed<br>
when i=2, j is 0,1,2     but 333   is printed<br>
when i=3, j is 0,1,2,3   but 4444  is printed<br>
when i=4, j is 0,1,2,3,4 but 55555 is printed<br>
So, whichever character is getting printed - ut is exactly row+1 in every iteration & hence the logic. And the number of times that character is getting printed is the number of times te col loop is working for every value of row.
