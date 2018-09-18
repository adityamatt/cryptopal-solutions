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
    if (input1.length()!=input2.length())
    {
        cout<<"ERROR:Unequal length inputs";
        return -1;
    }
    int n=input1.length();
    int ans=0;
    for (int i=0;i<n;i++)
    {
        int tmp=((int)input1[i])^((int)input2[i]);
        while (tmp>0)
        {
            if (tmp & 1) ans++;
            tmp=tmp/2;
        }
    }
    return ans;
}
char find_xor_key(string input)
{
    int n=input.length();
    map<int,int> freq;
    for (int i=0;i<n;i++)
    {
        freq[do_xor(input[i],' ')]++;
    }
    char c=(char)freq.begin()->first;
    int f=freq.begin()->second;
    for (map<int,int>::iterator i=freq.begin();i!=freq.end();i++)
    {
        if (i->second> f)
        {
            f=i->second;
            c=(char)i->first;
        }
    }
    return c;
}
string break_(string input)
{
    map<float,int> store;
    int n=input.length();
    for (int key=2;key<=40;key++)
    {
        string input_copy=input;
        float total=0;
        string first="",second="",third="",four="";
        for (int i=0;i<key;i++)
        {
            first=first+input_copy[0];
            input_copy.erase(0,1);
        }
        for (int i=0;i<key;i++)
        {
            second=second+input_copy[0];
            input_copy.erase(0,1);
        }
         for (int i=0;i<key;i++)
        {
            third=third+input_copy[0];
            input_copy.erase(0,1);
        }
         for (int i=0;i<key;i++)
        {
            four=four+input_copy[0];
            input_copy.erase(0,1);
        }
        total=hamming_distance(first,second)+hamming_distance(first,third)+hamming_distance(first,four)+hamming_distance(second,third)+hamming_distance(second,four)+hamming_distance(third,four);
        total=total/key;
        total=total/6; //mean
        store[total]=key;
    }
//    for (map<float,int>::iterator i=store.begin();i!=store.end();i++)
//    {
//        cout<<i->first<<" "<<i->second<<endl;
//    }
    int key_length=store.begin()->second;
    string key="";
    for (int i=0;i<key_length;i++)
    {
        string basic="";
        int j=i;
        while (j<n)
        {
            basic=basic+input[j];
            j=j+key_length;
        }
        key=key+find_xor_key(basic);
    }
    return key;
}
//taken from online
static const std::string base64_chars = 
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
             "abcdefghijklmnopqrstuvwxyz"
             "0123456789+/";
static inline bool is_base64(unsigned char c) {
  return (isalnum(c) || (c == '+') || (c == '/'));
}


string base64_decode(std::string const& encoded_string) {
  int in_len = encoded_string.size();
  int i = 0;
  int j = 0;
  int in_ = 0;
  unsigned char char_array_4[4], char_array_3[3];
  std::string ret;

  while (in_len-- && ( encoded_string[in_] != '=') && is_base64(encoded_string[in_])) {
    char_array_4[i++] = encoded_string[in_]; in_++;
    if (i ==4) {
      for (i = 0; i <4; i++)
        char_array_4[i] = base64_chars.find(char_array_4[i]);

      char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
      char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
      char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

      for (i = 0; (i < 3); i++)
        ret += char_array_3[i];
      i = 0;
    }
  }

  if (i) {
    for (j = i; j <4; j++)
      char_array_4[j] = 0;

    for (j = 0; j <4; j++)
      char_array_4[j] = base64_chars.find(char_array_4[j]);

    char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
    char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
    char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

    for (j = 0; (j < i - 1); j++) ret += char_array_3[j];
  }

  return ret;
}
string decipher(string input,string key)
{
    string output="";
    int n=input.length();
    int j=0;
    for (int i=0;i<n;i++)
    {
        output=output+(char)do_xor(input[i],key[j]);
//        cout<<input[i]<<" "<<key[j]<<" "<<do_xor(input[i],key[j])<<endl;
        j++;
        if (j==key.length()) j=0;
    }
    return output;
}
int main()
{
    ifstream infile("6.input");
    string line;
    int i=0;
    string encrypted="";
    while (infile>>line)
    {
        encrypted=encrypted+(base64_decode(line));
        i++;
    }
//    cout<<hamming_distance("this is a test","wokka wokka!!!")<<endl;
    string key=break_(encrypted);
    cout<<decipher(encrypted,key)<<endl;
    return 0;
}
