#include<iostream>
#define li long long
using namespace std;
void solve()
{ 
    li n,m,k;
    cin>>n>>m>>k;
    double arr[n+1][m+1];
    for( li i=0;i<=n;i++)
    {
        for(li j=0;j<=m;j++)
        {
          if(i==0||j==0)
           arr[i][j]=0;
          else
          cin>>arr[i][j];
        
       }
    }
    for ( li i =0;i<=n;i++)
    {
        double prev=0;
        for( li j=0;j<=m;j++)
        {
            arr[i][j]+=prev;
            prev=arr[i][j];
            
        }
    }
    for ( li i=0;i<=m;i++)
    {
        double prev=0;
        for( li j=0;j<=n;j++)
        { 
            arr[j][i]+=prev;
            prev=arr[j][i];
        }
            
      
      
    } li m_min= min(m,n);
     li ans=0;
      for( li u=1;u<=m_min;u++)
      {
          for(li i=u;i<=n;i++)
          {
              for( li j=u;j<=m;j++)
              {
                  if((arr[i][j]+arr[i-u][j-u]-arr[i][j-u]-arr[i-u][j])/(u*u)>=k)
                  ans++;
              }
          }
      }cout<<ans<<endl;
}
              
      



int main() {
	li t;
	cin>>t;
	while(t--){
	    solve();
	}return 0;
}


