int reverse(int x){
    long int reverse = 0;
    while(x)
    {
        reverse = reverse * 10 + (x % 10);
        x /= 10;
    }
    if(reverse > INT_MAX || reverse < INT_MIN)
        return 0;
    return reverse;
}
