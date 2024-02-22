class Search:
    
    def __init__(self) -> None:
        pass
    
    '''The following function Performs Binary Search on an Descending List'''
    
    def Binary(list,target):
        lo=0
        hi=len(list)-1
    
        while lo<=hi:
            mid=(hi+lo)//2
        
            if list[mid]==target:
                if list[mid-1]==target:
                    return mid-1
                else:
                    return mid
        
            if list[mid]>target:
                lo=mid+1
        
            if list[mid]<target:
                hi=mid-1
            
        return -1

