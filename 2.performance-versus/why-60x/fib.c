long fib(long ord) {
    if (ord < 2) {
        return ord;
    }
    long ans = 1;  // ans=n=1
    long last = 0; // last=n=0
    for (int i=1; i<ord; i++) {
        ans = ans + last;
        last = ans - last;
    }
    return ans;
}
