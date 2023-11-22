    // # n = len ( s)
    // # pre[][] = int [n] [26]
    // # pre[0][s[0]-'a'] = 1
    // # for i from 1 to n:
    // #     for c from 0 to 26:
    // #         pre[i][c] = pre[i-1][c]
    // #     pre[ilis[i]-'a'j++
    // # ans = [1
    // # for query in queries:
    // #     current = 0
    // #     for c from 0 to 26:
    // #         freq = pre[query.r] - pre[query.l-1]
    // #         current += (freq* (freq+1)) /2 
    // #     ans. append (current)
    // # return ans
    
// # print(solve("abcaab", [[1,6]]))
#include<bits/stdc++.h>
using namespace std;
int main(){
    int num;
    cin>>num;
    cout<<"Input Number is "<<num<<endl;
}
