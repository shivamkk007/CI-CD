def Binary(list,target):
    lo=0
    hi=len(list)-1
    
    while lo<=hi:
        mid=(hi+lo)//2
        
        if list[mid]==target:
            return mid
        
        if list[mid]<target:
            lo=mid+1
        
        if list[mid]>target:
            hi=mid-1
            
    return "Not in List"

def test():
    
    assert Binary([1,2,4,5,6],4)==2
    
def test_custom():
    
    