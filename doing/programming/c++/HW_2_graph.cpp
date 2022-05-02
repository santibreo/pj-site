#include <vector>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <iostream>
#include <assert.h>
#include <math.h>

using namespace std;

/*****************************************************************************************
FRIEND FUNCTIONS
*****************************************************************************************/
template < typename T>
std::pair<bool, int> findInVector(const std::vector<T> &vec, const T val){
    std::pair <bool, int> result;
    result = std::make_pair(false, -1);
    for(int i=0; i < vec.size(); ++i){
        if(vec[i] == val){
            result.first = true;
            result.second = i;
        }
    }
    return result;
}

/*****************************************************************************************
GRAPH CLASS
* I have chosen the connectivity matrix implementation for the Graph.
* To define the graph you must indicate the number of vertices, the
* density and the distance range. The result is a random undirected
* graph, which is the course statement.
*****************************************************************************************/
class RandomGraph{
public:
    RandomGraph(int aVerticeNum, double aDensity, int aDistRange){
        // Check the input arguments are all valid
        assert(aVerticeNum >= 0 && aDensity >=0 && aDistRange > 0);
        // Define main attributes
        setVerticeNum(aVerticeNum);
        setDistRange(aDistRange);
        setDistMatrix(aDensity);
        setEdgeNum();
        setDensity();
    }
    // Get main RandomGraph attributes
    int getVerticeNum() const {
        return verticeNum;
    };
    int getEdgeNum() const {
        return edgeNum;
    };
    double getDensity() const {
        return density;
    };
    std::vector< std::vector<int> > getDistMatrix() const{
        return distMatrix;
    };
    // Get some specific info about graph
    int getEdgeDist(int node1, int node2) const{
        return distMatrix[node1][node2];
    };
    // Only show it, you can't get it. Just to make some checks
    void showDistMatrix() {
        for (int i = 0; i < verticeNum; i++){
            for (int j = 0; j < verticeNum; ++j){
                cout << distMatrix[i][j] << ", ";
            };
            cout << endl;
        };
    };
    // MODIFYING GRAPH FUNCTIONS
    // Define new value for x - y link
    void setEdgeValue(int node1, int node2, int weight){
        assert(weight <= distRange);
        distMatrix[node1][node2] = weight;
        distMatrix[node2][node1] = weight;
        setEdgeNum();
        setDensity();
    };
    void deleteEdge(int node1, int node2){
        if (distMatrix[node1][node2] >= 0){
            distMatrix[node1][node2] = -1;
            distMatrix[node2][node1] = -1;
            setEdgeNum();
            setDensity();
        };
    };
    // INTERNAL GRAPH INFO
    // What nodes are linked to x
    std::vector<int> getNeighbours(int node) const{
        assert(node>=0 && node<=verticeNum);
        vector<int> list;
        for (int i=1; i <= verticeNum; i++){
            if (distMatrix[node][i] > 0){
                list.push_back(i);
            };
        };
        return list;
    };
    // List vertices in the graph
    std::vector<int> getVertices() const{
        vector<int> vertices;
        for (int i=1; i <= verticeNum; i++){
            vertices.push_back(i);
        }
        return vertices;
    }
    
private:
    // Number of vertices is untouchable
    int verticeNum;
    void setVerticeNum(int aVerticeNum){
        verticeNum = aVerticeNum;
    };
    // Distance range is untouchable
    int distRange;
    void setDistRange(int aDistRange){
        distRange = aDistRange;
    };
    // EVALUATED ARGUMENTS
    // Distances Matrix is untouchable
    std::vector< std::vector<int> > distMatrix;
    void setDistMatrix(double aDensity){
        // Using -1 for not existing edges
        distMatrix.resize(verticeNum, std::vector<int>(verticeNum, -1));
        srand(time(0)); // Initialize random seed
        // Fill the distances Matrix
        for (int i = 0; i < verticeNum; i++){
            for (int j = i; j < verticeNum; ++j){
                double prob = static_cast <double> (rand() % 100) / 99; // Probability number between 0 - 1
                if (j == i){ // Distance from one node to itself is 0
                    distMatrix[i][j] = 0;
                }else if (prob < aDensity){ // Random distance from one node to another
                    int weight = rand() % distRange + 1;
                    // Undirected = symetric matrix
                    distMatrix[i][j] = weight;
                    distMatrix[j][i] = weight;
                };
            };
        };
    };
    // Number of edges is untouchable
    int edgeNum;
    void setEdgeNum(){
        edgeNum = 0;
        for (int i = 0; i < verticeNum; i++){
            for (int j = i+1; j < verticeNum; ++j){
                if (distMatrix[i][j] > 0){
                    ++edgeNum;
                };
            };
        };
    };
    // Density is untouchable
    double density;
    void setDensity(){
        // Real density of the graph
        int poss_edges = floor((pow(verticeNum, 2) + verticeNum) /2);
        density = static_cast <double> (edgeNum) / poss_edges;
    };
};

/*****************************************************************************************
SHORT PATH CLASS
*****************************************************************************************/
class ShortPath{
public:
    ShortPath(RandomGraph graph, int node1, int node2){
        // Define main attributes
        setTotalNodes(graph.getVerticeNum());
        std::pair<std::vector<int>, int> dijOut = dijkstra(graph, node1, node2);
        setDistance(dijOut.second);
        setItinerary(dijOut.first, node1);
    };
    // Distance and itinerary
    int getDistance(){
        return distance;
    };
    std::vector<int> getItinerary(){
        return itinerary; 
    }
private:
    // Total nodes of the Graph
    int totalNodes;
    void setTotalNodes(int verticeNum){
        totalNodes = verticeNum;
    };
    int distance;
    void setDistance(int dist){
        distance = dist;
    };
    // Itinerary from source to end
    std::vector<int> itinerary;
    void setItinerary(std::vector<int> it_bad, int src){
        // Remove the first -1
        it_bad.erase(it_bad.begin(), it_bad.begin() +1);
        // Save only best itinerary
        for(int i = 0; i < it_bad.size(); ++i){
            std::pair <bool, int> result = findInVector(itinerary, it_bad[i]);
            if(result.first){
                itinerary.erase(itinerary.begin() + result.second -1, itinerary.end());
            };
            itinerary.insert(itinerary.end(), it_bad[i]);
        };
    };
    // Function to select the node that is at minimun distance
    int minDistance(std::vector<int> distances, std::vector<bool> closedSet){ 
        // Initialize min value
        int min = INT_MAX; int min_index = -1;
        for(int node = 0; node < totalNodes; node++) 
            if(!closedSet[node] && distances[node] < min)
                min = distances[node], min_index = node;
            return min_index;
    };
    /* Function that implements Dijkstra's source - end shortest path algorithm 
    * for a graph represented using adjacency matrix*/
    std::pair<std::vector<int>, int> dijkstra(RandomGraph graph, int src, int end){
        std::pair< std::vector<int>, int > result;
        std::vector< std::vector<int> > distMatrix = graph.getDistMatrix(); 
        // Initialize distances vector
        std::vector<int> dist (totalNodes, INT_MAX);
        dist[src] = 0; // Distance from the source node to itself
        // Initialize closed Set (boolean)
        std::vector<bool> closedSet (totalNodes, false);
        // Initialize itinerary vector
        std::vector<int> it_wrong;
        std::vector<int> prev_step (totalNodes, -1);
        while(src != -1 && src != end){
            src = minDistance(dist, closedSet);
            // Distances of nodes from current node
            std::vector<int> currNodeDist = distMatrix[src];
            // Update dist value of the adjacent vertices of the picked vertex. 
            for(int node = 0; node < totalNodes; ++node){
                /* Update dist[node] only if is not in closedSet and new distance
                * is lower than previous one.*/
                if(currNodeDist[node] > 0){
                    int new_dist = dist[src] + currNodeDist[node];
                    if(!closedSet[node] && new_dist < dist[node]){
                        dist[node] = new_dist;
                        prev_step[node] = src;
                        cout << src << " - " << new_dist << " -> " << node << "; ";
                    };
                };
            };
            cout << endl;
            // Add source to the closedSet
            closedSet[src] = true;
            // Add step to itinerary
            it_wrong.insert(it_wrong.end(), prev_step[src]);
        }
        it_wrong.insert(it_wrong.end(), end);
        result.first = it_wrong;
        result.second = dist[end];
        return result;
    };
};

/*****************************************************************************************
 MAIN FUNCTION
*****************************************************************************************/
int main(){
    int vn = 50;
    RandomGraph G(vn, 0.1, 10);
    ShortPath BP(G, 1, 35);
    cout << BP.getDistance() << endl;
    std::vector<int> aaa = BP.getItinerary();
    for(int i=0; i < aaa.size(); ++i){
        cout << aaa[i] << " -> ";
    }
    return 0;
}

/*****************************************************************************************
REFERENCES
 https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
*****************************************************************************************/