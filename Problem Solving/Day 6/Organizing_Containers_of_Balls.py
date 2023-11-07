# /***
# David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.
# David wants to perform some number of swap operations such that:
#   Each container contains only balls of the same type.
#   No two balls of the same type are located in different containers.

# Function Description:
# Complete the organizingContainers function in the editor below.
# organizingContainers has the following parameter(s):
# int containter[n][m]: a two dimensional array of integers that represent the number of balls of each color in each container

# Returns:
# string: either Possible or Impossible

# Input Format:
# The first line contains an integer q, the number of queries.
# Each of the next q sets of lines is as follows:
#   The first line contains an integer n, the number of containers (rows) and ball types (columns).
#   Each of the next n lines contains  space-separated integers describing row containers[i].
# ***/

POSSIBLE= "Possible"
IMPOSSIBLE="Impossible"

def organizingContainers(container):
    print(container)
    
    countByType=[0]* len(container[0])
    countByContainer=[sum(x) for x in container]
    for Ci in container: 
        print ("Ci=", Ci)
        for j in range(len(Ci)):
            print(" j=",j)
            countByType[j]+=Ci[j]

    countByContainer.sort()
    countByType.sort()
    print('Count By Types:',countByType)
    print('Count By Container:',countByContainer)
    return POSSIBLE if countByContainer==countByType else IMPOSSIBLE

