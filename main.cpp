#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <errno.h>
using namespace std;

void prime(int n)
{
    int i;
    bool isPrime = true;

    for(i = 2; i <= n/2; ++i)
    {
        if(n%i == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime && n != 0){
        cout<<n<<" is a prime number."<<endl;
    }
    else{
        cout<<n<<" is not a prime number."<<endl;
    }
}


int main(int argc, char* argv[])
{
    if(argc<2)
    {
        cout<<"You did not pass any number."<< endl;
        return -1;
    }
    else
    {
        char* p;
        errno=0;
        int N = (int) strtol(argv[1], &p, 10);

        if (*p != '\0' || errno !=0 || N > INT_MAX)
        {
        cout<<"You entered an invalid character "<<
        "or it is bigger than int."<<endl;
        return -1;
        }
        else
        {
        prime(N);
        }
    }
return 0;
}
