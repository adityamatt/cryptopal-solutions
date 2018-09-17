#include <bits/stdc++.h>
using namespace std;
int convert(char c)
{
    if (c>='0' && c<='9') return c-'0';
    if (c>='a' && c<='z') return c-'a'+10;
    if (c>='A' && c<='Z') return c-'A'+10;
}
char convert(int i)
{
    if (i<=9 && i>=0) return i+'0';
    return i+'a'-10;
}
string do_xor(string input1,string input2)
{
    int n=input1.length();
    if (input2.length()!=n) return "Unequal Length input";
    string output="";
    for (int i=0;i<n;i++)
    {
        int f1=convert(input1[i]);
        int f2=convert(input2[i]);
        output=output+convert(f1^f2);
    }
    return output;
}
int main()
{
    string input1="1c0111001f010100061a024b53535009181c";
    string input2="686974207468652062756c6c277320657965";
    cout<<do_xor(input1,input2)<<endl;
    return 0;
}
