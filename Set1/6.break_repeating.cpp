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
void prepare(map<char,int>& map_data)
{
    for (char c='A';c<='Z';c++)
    {
        map_data[c]=(c-'A');
    }
    for (char c='a';c<='z';c++)
    {
        map_data[c]=c-'a'+26;
    }
    for (char c='0';c<='9';c++)
    {
        map_data[c]=c-'0'+52;
    }
    map_data['+']=62;
    map_data['/']=63;
}

string base64_to_hex(string input)
{
    map<char,int> mapping;
    prepare(mapping);
    
    while (input.length()%2) input='0'+input;
    string output="";
    while (input.length())
    {
        int index1=mapping[input[0]];
        int index2=mapping[input[1]];
        char c1=convert(index1/4);
        char c2=convert((index1-(index1/4)*4)*4 + (index2/16));
        char c3=convert(index2-(index2/16)*16);
        output=output+c1+c2+c3;
        input.erase(0,2);
    }
    return output;
}
int hamming_distance(string input1,string input2)
{
    if (input.length()!=input2.length())
    {
        cout<<"ERROR:Unequal length inputs"
        return -1;
    }
}
int main()
{
    ifstream infile("6.input");
    string line;
    int i=0;
    vector<string> encrypted;
    while (infile>>line)
    {
        encrypted.push_back(base64_to_hex(line));
        cout<<base64_to_hex(line)<<endl;
        i++;
    }
    for (int i=0;i<encrypted.size();i++)
    {
        cout<<encrypted[i]<<endl;
    }
    
    return 0;
}
