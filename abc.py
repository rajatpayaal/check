# Python program to print all distinct  
# elements in a given array 
  
def solve(x,y, n): 
      
    # First sort the array so that  
    # all occurrences become consecutive 
    arr.sort(); 
    # Traverse the sorted array 
    for i in range(n): 
          
        # Move the index ahead while there are duplicates 
        if(i < n-1 and arr[i] == x[i+1]): 
            while (i < n-1 and (x[i] == x[i+1])): 
                i+=1; 
            
              
  
        # prlast occurrence of the current element 
        else: 
            print(x[i], end=" "); 
  
# Driver code 
x = [40,30,10,50,120]; 
n = len(x); 
x.sort(reverse=True)
print(x)
x.sort()
print(x[-1]) 

  
# This code has been contributed by 29AjayKumar 