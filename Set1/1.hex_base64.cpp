#include <bits/stdc++.h>
using namespace std;
void prepare(map<int,char>& map_data)
{
    for (int i='A';i<='Z';i++)
    {
        map_data[i-'A']=i;
    }
    for (char c='a';c<='z';c++)
    {
        map_data[c-'a'+26]=c;
    }
    for (char c='0';c<='9';c++)
    {
        map_data[c-'0'+52]=c;
    }
    map_data[62]='+';
    map_data[63]='/';
}
int convert(char c)
{
    if (c>='0' && c<='9') return c-'0';
    if (c>='a' && c<='z') return c-'a'+10;
    if (c>='A' && c<='Z') return c-'A'+10;
}
string hex_to_base64(string input)
{
    while (input.length()%6)
    {
        input='0'+input;
    }
    map<int,char> data;
    prepare(data);
    string output="";
    while (input.length())
    {
        int c1=convert(input[0]);
        int c2=convert(input[1]);
        int c3=convert(input[2]);
        int index1=c1*4+c2/4;
        int index2=(c2-(c2/4)*4)*16+c3;
        output=output+data[index1]+data[index2];
        input.erase(0,3);
    }
    return output;
}
int main()
{
    
    string hex="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    cout<<hex_to_base64(hex)<<endl;
    
}
