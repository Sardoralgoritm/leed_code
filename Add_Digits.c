int my_func(int n)
{
    int ans = 0;
    int cnt;
    while(n)
    {
        cnt = n % 10;
        ans += cnt;
        n /= 10;
    }
    return ans;
}
int addDigits(int num){
    while(num > 9)
    {
        num = my_func(num);
    }
    return num;
}
