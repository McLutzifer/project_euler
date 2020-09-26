//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?


#include <iostream>
#include <vector>

using namespace std;


int prime (long long z, vector<long long> &vec)
{
    int count = 0;
    for (int y = 3; y < z; ++y)
    {
        if ( z%y == 0)
        {
            ++count;
            if (count > 0)
            {
                break;
            }
        }
    }

    if (count == 0 && z != 1)
        {
            //cout << z << " is prime " << endl;
            vec.push_back(z);
        }
}


int main()
{
    long long test = 600851475143;
    vector<long long> prime_numbers{};
    vector<long long> myVec{};

    for (int i = 2; i < test; ++i)
    {
        if (test % i == 0)
        {
            prime_numbers.push_back (i);
        }
    }

    for (long long x : prime_numbers)
    {
        prime(x, myVec);
    }

    long long max = 0;
    for (long long x : myVec)
    {
        if (x > max)
        {
            max = x;
        }
    }

    cout << "What is the largest prime factor of the number 600851475143: \n" << max << endl;

 return 0;
}


// 6857

