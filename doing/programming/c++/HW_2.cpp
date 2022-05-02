#ifndef GRAPH_H
#define GRAPH_H

#include <vector>

// I think the best way to define graph is via adjacent matrix
class Graph{
    public:
        Graph(){}
        
        Graph(int verticeNum);
        
        Graph(int verticeNum, double density);
        
        int getVerticeNum() const {
            return verticeNum;
        }
        
        int getEdgeNum() const {
            return edgeNum;
        }
        
        // Is x linked to y
        bool adjacent(int x, int y) const;
        
        // What nodes are linked to x
        std::vector<int> neighbours(int x) const;
        
        // List vertices in the graph
        std::vector<int> getVertices() const;
        
        bool addEdge(int x, int y, int value);
        
        bool deleteEdge(int x, int y);
        
        int getEdgeValue(int x, int y) const;
        
        void setEdgeValue(int x, int y, int value);
    
    private:
        int edgeNum;
        int verticeNum;
        std::vector<std::vector<int>> adMatrix;
};

#endif