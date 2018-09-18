#include <bits/stdc++.h>
using namespace std;
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
int do_xor(char c1,char c2)
{

    return (int)(int(c1)^int(c2));
}
string decipher(string input,string key)
{
    string output="";
    int n=input.length();
    int j=0;
    for (int i=0;i<n;i++)
    {
        cout<<(int)input[i]<<" "<<(int)key[j]<<" "<<do_xor(input[i],key[j])<<endl;
        output=output+(char)do_xor(input[i],key[j]);
//        cout<<input[i]<<" "<<key[j]<<" "<<do_xor(input[i],key[j])<<endl;
        j++;
        if (j==key.length()) j=0;
    }
    return output;
}
int main()
{
    string key="YELLOW SUBMARINE";
    ifstream infile("7.input");
    string line;
    int i=0;
    string encrypted="";
    while (infile>>line)
    {
        encrypted=encrypted+(base64_decode(line));
        i++;
    }
//    cout<<encrypted<<endl;
    string decrypted=decipher(encrypted,key);
    cout<<decrypted<<endl;
}

