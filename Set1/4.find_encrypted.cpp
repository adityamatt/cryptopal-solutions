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
char do_xor(char c1,char c2)
{

    return (char)(int(c1)^int(c2));
}
bool is_valid(char c)
{
    if (c<32) return false;
    if (c>126) return false;
    return true;
}
string decrypt(string input,char key)
{
    string output="";
    while (input.length())
    {
        int c1=convert(input[0]);
        int c2=convert(input[1]);
        int c=c1*16+c2;
//        cout<<c1<<" "<<c2<<" "<<c<<endl;
        if (is_valid(do_xor(c,key))==false) return output;
        output=output+do_xor(c,key);
        input.erase(0,2);
    }
    return output;
}

string find_xor_string(string input)
{
    string consider=decrypt(input,' ');
    int a[256]={};
    for (int i=0;i<consider.length();i++) a[consider[i]]++;
    int max=0;
    for (int i=0;i<256;i++) 
    {
        if (a[max]<a[i])
        {
            max=i;
        }
    }
    return decrypt(input,(char)(max));
}
int score(string input)
{
    int c=0;
    for (int i=0;i<input.length();i++)
    {
        if (input[i]==' ') c++;
    }
    return c;
}
int main()
{
    ifstream infile("4.input");
    string line;
    int sc=0;
    string encrypted;
    int store=0;
    int i=0;
    while (infile>>line)
    {
//        cout<<i+1<<"\t"<<line<<endl;
        if (sc<score(find_xor_string(line)))
        {
            encrypted=string(line);
            sc=score(find_xor_string(line));
            store=i;
        }
        i++;
    }
    cout<<store+1<<" "<<encrypted<<endl;
    cout<<find_xor_string(encrypted)<<endl;
    return 0;
}
