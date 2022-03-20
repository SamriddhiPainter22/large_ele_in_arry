arr=[25,65,85,56,21,100]

max=arr[0]

for i in range(0,len(arr)):
    if(arr[i]>max):
        max=arr[i]

print("Largest array present in the given array :  "+str(max))