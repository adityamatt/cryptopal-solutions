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
int do_xor(char c1,char c2)
{

    return (int)(int(c1)^int(c2));
}
string repeat(string input,string key)
{
    string output="";
    int key_pos=0;
    for (int i=0;i<input.length();i++)
    {
        int xored=do_xor(input[i],key[key_pos++]);
        if (key_pos>=key.length()) key_pos=0;
        int latter=xored/16;
        int first=xored-latter*16;
//        cout<<latter<<" "<<first<<"\t"<<convert(latter)<<" "<<convert(first)<<endl;
        output=output+string(1,convert(latter))+string(1,convert(first)); 
    }
    return output;
}

int main()
{
    string input1="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal";
    cout<<repeat(input1,"ICE")<<endl;
//    cout<<repeat(input2,"ICE")<<endl;
    return 0;
}
