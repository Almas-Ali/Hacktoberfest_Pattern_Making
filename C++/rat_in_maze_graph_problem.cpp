vector<string> vec ;

    void path ( int src , vector<int> adj[] , string &str , vector<bool> vis , int &n )
    {
        if ( src == (n*n) -1 )
        {
            vec.push_back(str);
            str.pop_back();
            return ;
        }

        vis[src] = 1 ;
        for ( auto i:adj[src] )
        {
            if ( vis[i] == 0 )
            {
                if ( i == src -1 )
                str += "L" ;
                else if ( i == src +1 )
                str += "R";
                else if ( i == src -n )
                str += "U";
                else if ( i == src +n )
                str += "D" ;

                path ( i , adj , str , vis , n );
            }
        }
        str.pop_back();
    }


    vector<string> findPath(vector<vector<int>> &m, int n) {
        // Your code goes here

        if ( m[0][0] == 0 || m[n-1][n-1] == 0 )
        return vec ;

        vector<int> adj[n*n] ;

        for ( int i=0 ; i < n ; i++ )
        {
            for ( int j=0 ; j < n ; j++ )
            {
                int a = i*n + j ;
                if ( i > 0 && m[i-1][j] == 1 )
                {
                    adj[a].push_back( (i-1)*n + j );
                }
                if ( i < n-1 && m[i+1][j] == 1 )
                {
                    adj[a].push_back( (i+1)*n + j );
                }
                if ( j > 0 && m[i][j-1] == 1 )
                {
                    adj[a].push_back( i*n + j-1 );
                }
                if ( j < n-1 && m[i][j+1] == 1 )
                {
                    adj[a].push_back( i*n + j + 1 );
                }
            }
        }
        string str ;
        vector<bool> vis ( n*n , 0 ) ;
        path ( 0 , adj , str , vis , n );

        return vec ;
    }
