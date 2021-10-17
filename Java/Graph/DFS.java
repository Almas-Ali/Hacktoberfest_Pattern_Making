import java.io.*;
import java.util.*;

public class graph_dfs {
    static void dfsGraph(ArrayList<Integer> dfs,boolean[] vis, int node, ArrayList<ArrayList<Integer>>adj)
    {
          dfs.add(node);
          vis[node]=true;
                    for(int j:adj.get(node))
                    {
                        if(!vis[j])
                        {
                            vis[j]=true;
                            dfsGraph(dfs, vis, j, adj);
                        }
                    }
    }
    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList<Integer>> adj= new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        for(int i=1;i<=V+1;i++)
            adj.add(new ArrayList<>());

        adj.get(1).add(2);

        adj.get(2).add(1);
        adj.get(2).add(3);
        adj.get(2).add(7);

        adj.get(3).add(2);
        adj.get(3).add(5);

        adj.get(4).add(6);

        adj.get(5).add(3);
        adj.get(5).add(7);

        adj.get(6).add(4);

        adj.get(7).add(5);
        adj.get(7).add(2);

        System.out.println("DFS Traversal is: ");
        ArrayList<Integer> dfs= new ArrayList<>();
        boolean[] vis= new boolean[V+1];

        for(int i=1;i<=V;i++) {
            if (!vis[i]) {
                dfsGraph(dfs, vis, i, adj);
            }
        }
        System.out.println(dfs);
    }
}

/*  Graph structure here:

  1--2          4--6
    | \
   |   3
   |   |
   7--5

    */
