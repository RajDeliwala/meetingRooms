#Don't have access to leetcode premium for this problem so I'm just dropping the solution code here

function():

#Sort intervals list via built in sort() function / nLogn
intervals.sort()

#Need a global var to compare with start point, initalize to -1 because start can be 0
last_end = 1

#Loop through sorted list and compare each tuples times
for start, end in intervals:
  #Valid condition to continue
  if start >= last_end:
    last_end = end
  else:
    #We have an overlap
    return False
#return true, we have no overlap 
return True 
