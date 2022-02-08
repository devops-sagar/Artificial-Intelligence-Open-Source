class clusterCircle:

    def findOverlap(self ,ip):
        '''
        A function that finds the overlapping  circles and returns a list of tuples of the
        overlapped circles.
        '''
        cluster_list=[]
        for circle in range(len(ip)):
            for circle2 in range(len(ip)):
                
                #Optimized for avoiding rechecking of already examined circles for overlap
                if circle>=circle2:                                                                 
                    continue

                #Logic to find whether circles overlap
                sumofradii= (ip[circle][2]+ip[circle2][2])**2
                distance = ((ip[circle2][0]-ip[circle][0])*2)+((ip[circle2][1]-ip[circle][1])*2)
                if distance<sumofradii:
                    cluster_list.append((ip.index(ip[circle]) ,ip.index(ip[circle2])))
        
        return cluster_list 

    def findClusters(self,edges, vertices):
        '''
        This function is responsible to find the disjoint sets which
        contain different, individual clusters if present.
        '''

        def makeSet(x):
            return frozenset([x])

        # Create a meta-set/root array to 
        sets = set([makeSet(v) for v in vertices])

        # Find a set with element x in a list of all sets
        def findSet(x):
            for subset in sets:
                if x in subset:
                    return subset

        # Form a combined set containing all elements of both sets.
        def setUnion(set1, set2):
            sets.add(frozenset.union(set1, set2))
            sets.remove(set1)
            sets.remove(set2)

        # Finding the connected components
        for (u, v) in edges:
            set1 = findSet(u)
            set2 = findSet(v)

            if set1 != set2:
                setUnion(set1, set2)

        #Create a list of clusters
        #Example: [{3, 4, 5, 6}, {0, 1, 2}], where the elements inside the set denote input indices 
        list_of_clusters=[]
        for individual_sets in sets:
            list_of_clusters.append(set(individual_sets))
        return list_of_clusters
    
    
    
    def removeCircle(self,ip):
        
        outputlist=[]

        #Call our function on input to find overlaps of the circles
        clusters = self.findOverlap(ip)

        #Pass the recently found list of tuples of overlapping circles as edge while the number of circles = number of vertices
        list_of_clusters= self.findClusters(clusters,[x for x in range(len(ip)) if len(clusters)!=0])
        if len(list_of_clusters)==0:
            return ip
        #print(list_of_clusters,'list of clusters')
        for cluster_list in list_of_clusters:
            #print(len(cluster_list),'length')

            maxarea=0
            for i in (cluster_list):
                area = 3.14159*ip[i][2]*ip[i][2]
                if area>maxarea:
                    maxarea=area
                    circlemax=ip[i]

                    #A holder which holds the index for maximum area circle
                    index=i

            #print(maxarea,i)

            #Used to find circles other than the circle with highest area.
            for j in cluster_list:
                if j==index:
                    outputlist.append(ip[j])
        return outputlist
obj = clusterCircle()
#TEST CASE 1 - Provided in the assignment
input_1 =[(1,3,0.7),(2,3,0.4),(3,3,0.9)]
expected_output_1= True

#TEST CASE 2 - Provided in the assignment
input_2 =[(1.5,1.5,1.3),(4,4,0.7)]
expected_output_2= False

#TEST CASE 3 - Provided in the assignment
input_3 =[(0.5,0.5,0.5),(1.5,1.5,1.1),(0.7,0.7,0.4),(4,4,0.7)]
expected_output_3= False

result1 = obj.removeCircle(input_1)
if len(result1) == 1:
    res1 = True
else:
    res1 = False

print('INPUT1:',input_1)
print('OUTPUT1',res1)

result2 = obj.removeCircle(input_2)
if len(result2) == 1:
    res2 = True
else:
    res2 = False

print('INPUT2:',input_2)
print('OUTPUT2',res2)

result3 = obj.removeCircle(input_3)
if len(result3) == 1:
    res3 = True
else:
    res3 = False

print('INPUT3:',input_3)
print('OUTPUT3',res3)