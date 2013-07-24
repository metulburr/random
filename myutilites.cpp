#include <iostream>

#include <cstdlib> //randint
#include <ctime> //randint
using namespace std;


class Utility{
        bool srand_has_exc;
    public:
    
        Utility(){
            srand_has_exc = false;
        }
        
        
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
        
        string reverse(string s){
            return string(s.rbegin(), s.rend());
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

}

int main(){
    test();
}
