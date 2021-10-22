import java.util.ArrayList;

/* a undirected graph.
    0 ------ 1
    |     /   |\  
    |    /    | \     
    |   /     |   2
    |  /      | /
    4---------3/
*/
public class Graph {

    // v = no of vertices.
    private int v = -1;
    //adjacency list will represent edges in a graph.

    /*
        one vertex will be connected with multiple vertices
        so that will need an "ArrayList" of array-lists
        (like an 2-D array where i and j will represent an edge)
    */
    private ArrayList< ArrayList<Integer> > adjList = null;
    public Graph(int v) {

        this.v = v;
        adjList = new ArrayList<>(v);

        for(int i = 0; i<this.v; i++) { 
            adjList.add(new ArrayList<Integer>());
        }
    }
    // a function to add edges.
    private void addEdge(int src, int des) {

        adjList.get(src).add(des);
        adjList.get(des).add(src);
    }

    public void printGraph() {
        for(int i = 0; i< adjList.size(); i++) {

            System.out.print(i + " -> ");
            for(int j = 0; j<adjList.get(i).size(); j++) {
                System.out.print(adjList.get(i).get(j)+ " ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args) {
        Graph graph = new Graph(5);

        graph.addEdge(0, 1);
        graph.addEdge(0, 4);
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(1, 4);
        graph.addEdge(2, 3);
        graph.addEdge(3, 4);
        graph.printGraph();

    }
}