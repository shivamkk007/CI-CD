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
        
        if list[mid]<target:
            lo=mid+1
        
        if list[mid]>target:
            hi=mid-1
            
    return "Not in List"

def test():
    
    assert Binary([1,2,4,5,6],4)==2
    assert Binary([1,2,4,5,5,6],5)==3
    assert Binary([1,2,4,5,6,7,8],8)==6
    
# Push V1.3

# def test_custom():
    
#     tests=[]

#     tests.append({
#         'input':{
#             'cards':[],
#             'query':7
#         }, 'output':-1
#     })
#     tests.append({
#         'input':{
#             'cards':[10,6,4,2,1],
#             'query':7
#         }, 'output':-1
#     })
#     tests.append({
#         'input':{
#             'cards':[9,7,6,4,3,2,1],
#             'query':7
#         }, 'output':1
#     })
#     tests.append({
#         'input':{
#             'cards':[9,8,7,7,6,5,4,3],
#             'query':7
#         }, 'output':2
#     })
#     tests.append({
#         'input':{
#             'cards':[19,18,17,17,16,5,4,3],
#             'query':4
#         }, 'output':6
#     })