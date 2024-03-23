
import math
def gini(S):
    temp = 0
    totalInstances = sum(list)
    for val in range(len(S)):
        temp += (S[val]/totalInstances)*(S[val]/totalInstances)
    temp = 1 - temp 
    return temp

def WeightedAverageGini(root,split1,split2):
    totalInstances1 = sum(split1)
    totalInstances2 = sum(split2)
    totalInstances3 = sum(root)
    return ((totalInstances1/totalInstances3)*(gini(split1))+(totalInstances2/totalInstances3)*(gini(split2)))

def WeightedAverageEntropy(root,split1,split2):
    totalInstances1 = sum(split1)
    totalInstances2 = sum(split2)
    totalInstances3 = sum(root)
    return ((totalInstances1/totalInstances3)*(entropy(split1))+(totalInstances2/totalInstances3)*(entropy(split2)))

def entropy(list):
    temp = 0
    totalInstances = sum(list)
    for val in range(len(list)):
        if list[val]/totalInstances != 0:
            temp += (list[val]/totalInstances) * math.log2((list[val]/totalInstances))
    return temp

testNode = [10,10,130]
rootNode = [100,50,25,25]
choice1Left = [25,50,25,0]
choice1Right = [75,0,0,25]
choice2Left = [50,50,25,25]
choice2Right = [50,0,0,0]

test1Node = [200,100,100,100,100]
testSR1Node = [200,0,0,0,0,0]
testSL1Node = [0,100,100,100,100,100]
testSR2Node = [200,0,0,100,100,100]
testSL2Node = [0,100,100,0,0,0]
"""
print("GINI Impurity Score")
print("Root Node -", gini(rootNode))
print("Split Choice 1:Left -", gini(choice1Left))
print("Split Choice 1:Right -", gini(choice1Right))
print("Split Choice 2:Left -", gini(choice2Left))
print("Split Choice 2:Right -", gini(choice2Right))

print()
print("Weighted Average")

print("Split choice 1: ",WeightedAverage([100,50,25,25],[25,50,25,0],[75,0,0,25]))
print("Split choice 2: ",WeightedAverage([100,50,25,25],[50,50,25,25],[50,0,0,0]))
"""
"""
print(entropy(testNode))
"""
print("Entropy Score")
print("Root Node -", entropy(rootNode))
print("Split Choice 1:Left -", entropy(choice1Left))
print("Split Choice 1:Right -", entropy(choice1Right))
print("Split Choice 2:Left -", entropy(choice2Left))
print("Split Choice 2:Right -", entropy(choice2Right))

print()

print("Split choice 1: ",WeightedAverageEntropy(rootNode,choice1Left,choice1Right))
print("Split choice 2: ",WeightedAverageEntropy(rootNode,choice2Left,choice2Right))

print()

print("Split choice 1: ",WeightedAverageEntropy(test1Node,testSR1Node,testSL1Node))
print("Split choice 2: ",WeightedAverageEntropy(test1Node,testSR2Node,testSL2Node))
