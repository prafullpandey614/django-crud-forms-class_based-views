#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h> 
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>
 
using namespace std;
 
typedef long long ll;
typedef long double ld;
typedef pair<int,int> p32;
typedef pair<ll,ll> p64;
typedef pair<double,double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int> > vv32;
typedef vector<vector<ll> > vv64;
typedef vector<vector<p64> > vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i,e) for(ll i = 0; i < e; i++)
#define forsn(i,s,e) for(ll i = s; i < e; i++)
#define rforn(i,s) for(ll i = s; i >= 0; i--)
#define rforsn(i,s,e) for(ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout<<#x<<" = "<<x<<ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())
 
vector<int> query_game(int N , vector<int>&A , int Q , vector<vector<int>>P){
    int i = 0;
    vector<int>ans;
 while(i<P.size()){
        int a,b,c;
        a = P[i][0];
        b = P[i][1];
        c= P[i][2];
        b-- ; c--;

        if(a==1 ) reverse(A.begin(),A.end());
        else if(a==2 ){
            swap(A[b],A[c]);
        }
        else if(a==3) ans.push_back(A[b]);
     i++;
    }
    return ans ;
 
}
void solve(){

    int n ;
    cin>>n;
    v32 v(n);
    forn(i,n) cin>>v[i];
    int q;
    cin>>q;
    while(q--){
        int a,b,c;
        cin>>a>>b>>c;

        if(a==1 ) reverse(v.begin(),v.end());
        else if(a==2 ){
            swap(v[b],v[c]);
        }
        else if(a==3) cout<<v[b]<<endl;
    }

}
int main()
{
 fast_cin();
 ll t;
 cin >> t;
 for(int it=1;it<=t;it++) {

solve();
 }
 return 0;
}
