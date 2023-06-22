int climbStairs(int n){
    int a = 1;
    int b = 1;
    int c = 0;
    for(int i=0; i<n-1; i++){
        c = b + a;
        a = b;
        b = c;
    }
    if(n != 1)
        return c;
    else
        return 1;
}
