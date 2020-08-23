#include<iostream>
using namespace std;
int main()
{
  int n;
  cin>>n;
  int num=1;
  for(int i=1;i<=n;i++)
  {
      num=1;
      for(int j=1;j<=i;j++)
      {
        cout<<num<<" ";
        num=num*(i-j)/j;
      }
      cout<<endl;
  }
  return 0;
}
