//Contributed by: @with-mahimasingh

import java.io.*;
import java.util.*;

public class graph_bfs {

    static ArrayList<Integer> bfsGraph(int V, ArrayList<ArrayList<Integer>>adj)
    {
      ArrayList<Integer> bfs= new ArrayList<>();
      boolean[] vis= new boolean[V+1];

      for(int i=1;i<=V;i++)
      {
          if(!vis[i])
          {
              Queue<Integer> q=new LinkedList<>();
              q.add(i);
              vis[i]=true;

              while(!q.isEmpty())
              {
                  Integer node=q.poll();
                  bfs.add(node);

                  for(int j:adj.get(node))
                  {
                      if(vis[j]==false)
                      {
                          vis[j]=true;
                          q.add(j);
                      }
                  }
              }
          }
      }
      return bfs;
    }
    public static void main(String[] args) throws IOException {
        ArrayList<ArrayList<Integer>> adj= new ArrayList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st= new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        for(int i=1;i<=n+1;i++)
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

        System.out.println("BFS Traversal is: ");
        ArrayList<Integer> result= bfsGraph(n,adj);
        System.out.println(result);
    }
}

/*  Graph structure here:

  1--2          4--6
    | \
   |   3
   |   |
   7--5

    */
