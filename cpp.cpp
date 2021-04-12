#include<bits/stdc++.h>
#include <sys/time.h>
using namespace std;


long long get_usec() {
    timeval tv;
    gettimeofday(&tv, NULL);
    return (long long)tv.tv_sec * 1000000 + tv.tv_usec;
}

int fib(int n) {
    if (n < 2) {
        return n;
    }
    else {
        return fib(n - 1) + fib(n - 2);
    }
}

int main() {
    int mintrials = 5;
    vector<long long> v(mintrials);
    for (int i = 0; i < mintrials; ++i) {
        long long t = get_usec();
        int f = fib(35);
        t = get_usec() - t;
        v[i] = t;
    }
    sort(v.begin(), v.end());
    cout << setprecision(16) << v[0] * 1e-6 << ' ' << v[mintrials / 2] * 1e-6 << ' ' << v.back() * 1e-6 << '\n';
    return 0;
}
