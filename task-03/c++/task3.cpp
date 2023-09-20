#include <iostream>
using namespace std;

bool checkPrime(int n){
    for (int i=2; i<n; i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

int main(){
    int num;
    cout << "Enter Value ";
    cin >> num;
    int i;
    if ((num==1)||(num==0)){
        cout<<"No Prime in Range\n";
        return 0;
    }
    for (i=2;i<num;i++){
        if (checkPrime(i)){
            cout<<i<<" ";
        }

    }
    cout<<"\n";

}