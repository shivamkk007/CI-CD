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
            
    return "Not in List"

# def test():
    
#     assert Binary([1,2,4,5,6],4)==2
#     assert Binary([1,2,4,5,5,6],5)==3
#     assert Binary([1,2,4,5,6,7,8],8)==6
    
# Push V1.3

def test_custom():
    
    tests=[]

    tests.append({
        'input':{
            'list':[],
            'target':7
        }, 'output':-1
    })
    tests.append({
        'input':{
            'list':[10,6,4,2,1],
            'target':7
        }, 'output':-1
    })
    tests.append({
        'input':{
            'list':[9,7,6,4,3,2,1],
            'target':7
        }, 'output':1
    })
    tests.append({
        'input':{
            'list':[9,8,7,7,6,5,4,3],
            'target':7
        }, 'output':2
    })
    tests.append({
        'input':{
            'list':[19,18,17,17,16,5,4,3],
            'target':4
        }, 'output':6
    })
    
    for i,test in enumerate(tests):
        result=Binary(test['input']['list'], test['input']['target'])
        
        if(Binary(**test['input'])==test['output']):
            print(f"Test {i} Pass, \nTest Attributes",test,"Result:",result,"\n")
        else:
            print(f"Test{i} Failed, \nTest Attributes",test,"Result:",result,"\n")
        assert Binary(**test['input']==test['output'])
        
        
