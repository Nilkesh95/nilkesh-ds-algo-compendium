
## Approach

Here we see that:<br>
when row=0, col is 0,        but 1     is printed<br>
when row=1, col is 0,1       but 22    is printed<br>
when row=2, col is 0,1,2     but 333   is printed<br>
when row=3, col is 0,1,2,3   but 4444  is printed<br>
when row=4, col is 0,1,2,3,4 but 55555 is printed<br>
and so on...

So, whichever character is getting printed - it is exactly row+1 in every iteration & hence the logic. And the number of times that character is getting printed is the number of times the col loop is working for every value of row.
