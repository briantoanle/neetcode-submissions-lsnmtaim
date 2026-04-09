import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # i need to return the shortest distance from the start vertex to every vertex
        # build an adjacency list
        # adjacency list, with weight goes first,
        adj = {}
        # src = vertex id
        # edges = src, dst, weight
        # 
        # use a heap

        shortest_path = {}
        for i in range(n):
            shortest_path[i] = -1
        print(shortest_path)
        shortest_path[src] = 0
        for source, dst, weight in edges:
            if source not in adj:
                adj[source] = []
            adj[source].append((weight,dst))
        
        travel_queue = []
        # start the queue with distance = 0
        # put node into travel queue
        heapq.heappush(travel_queue,(0,src))
        #print(travel_queue)
        # I need to track the minimum distance of all of them
        

        while travel_queue:
            
            current_distance, current_node = heapq.heappop(travel_queue)
            #print(current_distance,"node",current_node)
            if current_node in adj:
                for weight, destination in adj[current_node]:
                    
                    temp_dist = weight + current_distance
                    #print('destination',destination, 'distance',temp_dist)
                    if shortest_path[destination] == -1 or shortest_path[destination] >= temp_dist:
                        #print('hit')
                        shortest_path[destination] = temp_dist
                        heapq.heappush(travel_queue,(temp_dist,destination))
        #print(shortest_path)
        return shortest_path
