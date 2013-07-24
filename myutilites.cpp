
#include <iostream>

#include <cstdlib> //randint
#include <ctime> //randint
#include <vector>
#include <fstream> 
#include <sstream>
using namespace std;


class Utility{
        bool srand_has_exc;
    public:
    
        Utility(){
            srand_has_exc = false;
        }
        
    //random
        int randint(int start=0, int maxnum=0, int increment=0){
            /*generate a random int max at maxnum, starting from start, increment add value to both
             * 
             * maxnum = max number minus one
             * start = number no less than accepted
             * increment = add increment to 
             */
            if (!srand_has_exc){
                srand(time(0)); 
                srand_has_exc = true;
            }
            int num=0;
            while (true){
                num = (rand() % maxnum) + increment; 
                if (start == 0)
                    return num;
                else if (num < start)
                    continue;
                else
                    break;
            }
            return num;
        }
        
    //basic operations
        string reverse(string s){
            return string(s.rbegin(), s.rend());
        }
        
        int max(int a[], int size){
            int mx = a[0];
            for(int i=0; i<size; i++){
                if(mx < a[i]){
                    mx = a[i];
                }
            }
            return mx;
        }
        int min(int a[], int size){
            int mn = a[0];
            for(int i=0; i<size; i++){
                if(mn > a[i]){
                    mn = a[i];
                }
            }
            return mn;
        }
        
        int max(vector<int> v){
            int mx = v[0];
            for (vector<int>::size_type i = 0; i != v.size(); i++) {
                if(mx < v[i]){
                    mx = v[i];
                }
            }
            return mx;
        }
        int min(vector<int> v){
            int mn = v[0];
            for (vector<int>::size_type i = 0; i != v.size(); i++) {
                if(mn > v[i]){
                    mn = v[i];
                }
            }
            return mn;
        }
        
        
        
    //file i/o
        void write(string filename, string data){
            ofstream f;
            f.open(filename);
            f << data;
            f.close();
        }

        void write(string filename, vector<string> v, string sep="\n"){
            ofstream f;
            f.open(filename);
            for (vector<int>::size_type i = 0; i != v.size(); i++) {
                f << v[i] << sep;
            }
            f.close();
        }

        void open(string filename){ //get entire line
            string s = "";
            ifstream f;
            f.open(filename);
            while(getline(f, s)){
                cout << s <<endl;
            }
            f.close();
        }
    
    
    //type conversion
        string int2str(int inter){
            //convert from int to string
            stringstream num_str;
            num_str << inter;
            return num_str.str();
        }
        int str2int(string str){
            //convert from string to int
            int i;
            stringstream ss(str);
            ss >> i;
            return i;
        }

        int flo2int(float floater){
            //convert from float to int
            //rounds down
            int i = static_cast<int>(floater);
            return i;
        }
        
        int dou2int(double d){
            //convert from double to int
            //rounds down
            int i = static_cast<int>(d);
            return i;
        }

        string cha2str(char ch){
            //ocnvert from cahr to string
            stringstream ss;
            string s;
            ss << ch;
            ss >> s;
            return s;
        }

        char str2cha(string stringer){
            //convert from string to char
            stringstream ss;
            char c;
            ss << stringer;
            ss >> c;
            return c;
        }

        int cha2asc(char ch){
            //convert from character to ascii number
            int i;
            i = (int)ch;
            return i;
        }

        char asc2cha(int num){
            //convert from ascii number to character
            char c;
            c = (char)num;
            return c;
        }
};


void test(){

    Utility util;
    
    
    for (int i=0; i<10; i++){
        cout << util.randint(5, 25) << ' ';
    }
    cout << endl;
    
    
    string gender[2] = {"Female", "Male"};
    for (int i=0; i<10; i++){
        cout << gender[util.randint(0,2)] << ' ';
    }
    cout << endl;
    
    
    cout << util.reverse("some random string") << endl;
    
    
    int a[10];
    for (int i=0; i<10; i++){
        a[i] = util.randint(0,25);
        cout << a[i] << ' ';
    }
    cout << endl;
    cout << "max num: " << util.max(a, 10) << endl;
    cout << "max num: " << util.min(a, 10) << endl;
    
    
    vector<int> v;
    for (int i=0; i<util.randint(3,10); i++){
        v.push_back(util.randint(0,100));
    }
    for (vector<int>::size_type i = 0; i != v.size(); i++) {
        cout << v[i] << ' ';
    }
    cout << endl;
    cout << util.max(v) << endl;
    cout << util.min(v) << endl;
    
    
    string name = "test.html";
    util.write(name, "some\nrandom\ndata");
    util.open(name);
    vector<string> s = {"test", "this", "right\nnow"};
    util.write(name, s);
    util.open(name);
    
    cout << util.int2str(1024).substr(0,3) << endl;
    cout << util.str2int("24") + 1 << endl;
    cout << util.flo2int(10.1) - 5 << endl;
    cout << util.cha2str('c') + "h" << endl;
    cout << util.str2cha("s") + 'h' << endl;
    cout << util.cha2asc('c') << endl;
    cout << util.asc2cha(99) << endl;
}




int main (){
    test();
}
