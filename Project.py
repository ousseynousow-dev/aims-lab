def mean(data):
  meann =sum(data)/len(data)
  return meann

# After finishing, I tried to verify my function without using `print`.
# I simply called the function, but nothing appeared.
# It was only later that I thought to use `print`, and then it worked.
def median(data):
  tri=sorted(data)
  for i in data:
    if len(data)%2!=0:
      go=len(data)//2
      return tri[go]
    else:
      go1=len(data)//2
      go2=(len(data)//2) -1
      good=(tri[go1] + tri[go2])/2
      print(tri)
      return good


print(median(([4, 8, 6, 7, 5, 8])))

# After finishing the code, I tested it with the example, and the output was correct.
# However, when I tested it with an example requiring an average—because the list length was even—
# it triggered the 'else' condition, resulting in the error:
# "list indices must be integers or slices, not float."
# I used '//' (integer division) to ensure the indices remained integers. Since I knew the length was even, 
# I could have omitted it, but—strangely—doing so produced an incorrect result.
# I had forgotten that list indexing starts at 0; therefore, I needed to use the middle index 
# along with the preceding index (-1) 
# instead of the following one (+1). Once I corrected this, I got the right result, and it worked perfectly.
