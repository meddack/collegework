#include<iostream>
using namespace std;
int main()
{


    int arr[100],n;
    cout<<"enter size of array"<<endl;
    cin>>n;
    cout<<"enter array"<<endl;
    int i=0;
    while(i<n)
    {
        cin>>arr[i];
        i++;
    }

    int sum=0;
    for(int i=0;i<n;i++)
    {
        sum=sum+arr[i];

    }
    cout<<"avg="<<sum/n<<endl;
}
