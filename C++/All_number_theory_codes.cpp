
//Github name: itz-arnav
//Contributed by Arnav Jha for hacktoberfest2022

#include <bits/stdc++.h>
using namespace std;

#define int            long long int
#define F              first
#define S              second
#define pb             push_back
#define si             set <int>
#define vi             vector <int>
#define pii            pair <int, int>
#define vpi            vector <pii>
#define vpp            vector <pair<int, pii>>
#define mii            map <int, int>
#define mpi            map <pii, int>
#define spi            set <pii>
#define endl           "\n"
#define double         long double
#define que_max        priority_queue <int>
#define que_min        priority_queue <int, vi, greater<int>>
#define yes cout<<"YES"<<endl
#define no cout<<"NO"<<endl
const int mod = 1000000007;
const int N = 100005;


inline long long normalize(long long x, long long mod) { x %= mod; if (x < 0) x += mod; return x; }

int power(int a, int b){
	int res = 1;
	while(b){
		if(b&1){
			res=(res*a)%mod;
			b--;
		}
		else{
			a=(a*a)%mod;
			b>>=1;
		}
	}
	return res;
}

int GCD(int a, int b){
	if(b == 0)
		return a;
	return GCD(b, a%b);
}

int LCM(int a, int b){
	return (a/GCD(a,b))*b;
}

struct GCD_type { int x, y, d; };
GCD_type ex_GCD(int a, int b)
{
    if (b == 0) return {1, 0, a};
    GCD_type pom = ex_GCD(b, a % b);
    return {pom.y, pom.x - a / b * pom.y, pom.d};
}

//CHINESE REMAINDER THEOREM
int crt(){
	int t;
	
	cin >> t;
	int a[t+2], n[t+2], ans, lcm;
    for(int i = 1; i <= t; i++){ 
    	cin >> a[i] >> n[i];
        normalize(a[i], n[i]);
    }
    ans = a[1];
    lcm = n[1];
    for(int i = 2; i <= t; i++)
    {
        auto pom = ex_GCD(lcm, n[i]);
        int x1 = pom.x;
        int d = pom.d;
        if((a[i] - ans) % d != 0) return cerr << "No solutions" << endl, 0;
        ans = normalize(ans + x1 * (a[i] - ans) / d % (n[i] / d) * lcm, lcm * n[i] / d);
        lcm = LCM(lcm, n[i]);
         // you can save time by replacing above lcm * n[i] /d by lcm = lcm * n[i] / d
    }
    cout << ans << " " << lcm << endl;
    return 0;
}

bool isPrime(int n){
	if(n < 2)
		return false;
	if(n < 4)
		return true;
	if(n%2 == 0 or n%3 == 0)
		return false;
	if(n < 25)
		return true;
	for(int i = 5; i*i <= n; i+=6){
		if(n%i == 0 or n%(i+2) == 0)
			return false;
	}
	return true;
}


int prime[N];
ll divisors[N];
ll sod[N];
ll lprime[N];
ll hprime[N];
vector <ll> pf;
vector <int> pr;

// STANDARD SIEVE

void sieve(int N){
	int i, j;
	memset(prime, 0, sizeof(prime));
	prime[0] = 1; prime[1] = 1;
	for(i = 2; i * i <= N; i++){
		if(prime[i] == 0){
			for(j = i * i; j <= N; j += i){
				prime[j] = 1;
			}
		}
	}
	for(i = 2; i <= N; i++){
		if(prime[i] == 0){
			pr.push_back(i);
		}
	}
}

// NUMBER OF DIVISORS USING SIEVE

void ndsieve(int N){
	int i, j;
	memset(divisors, 0, sizeof(divisors));
	for(i = 1; i <= N; i++){
		for(j = i; j <= N; j += i){
			divisors[j]++;
		}
	}
}

// SUM (OR PRODUCT) OF DIVISORS USING SIEVE 

void spdsieve(int N){
	int i, j;
	memset(sod, 0, sizeof(sod));
	for(i = 1; i <= N; i++){
		for(j = i; j <= N; j += i){
			sod[j] += i; // ( USE * FOR PRODUCT OF DIVISORS )
		}
	}
}

// LOWEST PRIME FACTOR USING SIEVE

void lpfsieve(int N){
	ll i, j;
	memset(lprime, 0, sizeof(lprime));
	lprime[1] = 0;
	for(i = 2; i <= N; i++){
		if(lprime[i] == 0){
            lprime[i] = i;
			for(j = i * i; j <= N; j += i){
				if(lprime[j] == 0){
					lprime[j] = i;
				}
			}
		}
	}
}

// HIGHEST PRIME FACTOR USING SIEVE AND PRIME FACTORIZATION

void hpfsieve(int N){
	int i, j;
	memset(hprime, 0, sizeof(hprime));
	hprime[1] = 0;
	for(i = 2; i <= N; i++){
		if(hprime[i] == 0){
			for(j = i; j <= N; j += i){
				hprime[j] = i;
			}
		}
	}
}

void pfactor(int a){
	pf.clear();
	while(a > 1){
		pf.push_back(hprime[a]);
		a /= hprime[a];
	}
}

// LINEAR RUNTIME SIEVE - LOWEST PRIME IN O(n)

void sieve1(int N){
	int i, j;
	memset(lprime, 0, sizeof(lprime));
	for(i = 2; i <= N; i++){
		if(lprime[i] == 0){
			lprime[i] = i;
			pr.push_back(i);
		}
		for(j = 0; j < pr.size() && pr[j] <= lprime[i] && i * pr[j] <= N; j++){
			lprime[i * pr[j]] = pr[j];
		}
	}
}

// SEGMENTED SIEVE - ( HIGH - LOW <= 10^6 )

void segSieve(int low, int high){
	int i, j;
	memset(segPrime, 0, sizeof(segPrime));

	for(i = 0; i < pr.size() && pr[i] * pr[i] <= high; i++){
		int L = floor(low / pr[i]) * pr[i];
		if(L < low){
			L += pr[i];
		}
		for(j = L; j <= high; j += pr[i]){
			if(pr[i] != j){
				segPrime[j - low] = 1;
			}
		}
		if(low == 1){
            segPrime[0] = 1;
		}
	}
}

//DIVISORS OF A NUMBER

vi findingdivisors(int n) {
    vi divisors ;
    for ( ll i = 1 ; i*i <= n ; i++) {
        if ( n%i == 0 ) {
            divisors.pb(i);
            if ( i != n/i ) divisors.pb(n/i);
        }
    }
    return divisors ;
}

//EULER PHI OF A NUMBER
int euler_phi(int n) {
    ll result = n ;
    for ( ll i = 2 ; i*i <= n ; i++) {
        if ( n % i == 0 ) {
            while(n%i == 0) n /= i ;
            result -= result/i ;
        }
    }
    if ( n > 1) result -= result/n ;
    return result ;
}

int32_t main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	#ifndef ONLINE_JUDGE
	freopen("input.txt",  "r",  stdin);
	freopen("output.txt", "w", stdout);
	#endif

	

	return 0;
}
