from Codes import Binary

'''The following is a Custom Test Function'''

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
        
        assert Binary(test['input']['list'], test['input']['target'])==test['output']
        
        
        if(Binary(test['input']['list'], test['input']['target'])==test['output']):
            print(f"Test {i} Passed! ")
        else:
            print(f"Test{i} Failed! ")
            
# Calling Custom Test Function
test_custom()