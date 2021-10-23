//Contributed by: @with-mahimasingh

//Articulation Point is a node on whose removal the graph can be broken down into 2 or more components.
//2 possible scenarios:
// i) low[it]>=tin[node] && parent!=-1 i.e. if non root is ap 
// ii) child>1 && parent==-1 i.e. is root is ap

class Solution
{
    //function to find and return all the APs present in given graph
    public int[] articulationPoints(int V, ArrayList<ArrayList<Integer>> adj)
    {
        
        int[] tin= new int[V];
        int[] low= new int[V];
        int[] vis= new int[V];
        int[] isArti= new int[V];
        int timer=0;
        for(int i=0;i<V;i++)
        {
            if(vis[i]==0)
             dfs(i,-1,tin,low,vis,isArti,timer, adj);
        }
        int c=0;
        for(int i=0;i<V;i++)
          if(isArti[i]==1)
             c++;
        if(c==0) return new int[]{-1}; //no AP present
        
        int arti[]= new int[c];
        int j=0;
        for(int i=0;i<V;i++)
          if(isArti[i]==1)
              arti[j++]=i;
              
        return arti;
    }
  
    void dfs(int node, int parent, int[] tin, int[] low, int[] vis, int[] isArti, int timer,  ArrayList<ArrayList<Integer>> adj)
    {
        vis[node]=1;
        tin[node]=low[node]=timer++;
        int child=0;
        for(int it: adj.get(node))
        {
            if(it==parent) continue; //not interested in parents. hence, continue with the next
            if(vis[it]==0) 
            {
                dfs(it,node,tin,low,vis,isArti,timer,adj);
                low[node]=Math.min(low[node],low[it]); //updating low with min value possible among its connected components
                
                if(low[it]>=tin[node] && parent!=-1)  //first case of AP
                  isArti[node]=1;
                child++;  
            }
            else
            low[node]=Math.min(low[node],tin[it]); //updating low with min value possible among its connected components
        }
        if(parent==-1 && child>1) isArti[node]=1; //second case of AP
    }
}


// TC: O(N+E)
// SC: O(N)
