def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        return None
    else:
        return a/b

def search (depth):
    """Returns a dictionary whose keys are integers and whose values are the
    minumum number of 5s needed to make the key using +-*/."""
    results = {5:1}
    newresults = {}
    for i in range(depth):
        for k1, v1 in results.iteritems():
            for k2, v2 in results.iteritems():
                for f in [add, subtract, multiply, divide]:
                    newkey = f(k1, k2)
                    newval = v1 + v2
                    if not newkey in results and newkey != None and (not newkey in newresults or newresults[newkey] > newval) and newval<=depth: 
                        newresults[newkey] = newval

        results = dict(newresults.items() + results.items())
    print results.items()
