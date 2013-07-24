#include <iostream>

#include <cstdlib> //randint
#include <ctime> //randint
#include <vector>
#include <fstream> 
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

}




int main (){
    test();
}
