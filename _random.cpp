
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>

class Random{
    public:
        Random(){
            srand(time(0));
        }
        
        //return element from given vector
        template <class T> 
        T choice(std::vector<T> v){
            int ind = rand() % v.size();
            return v[ind];
        }
        
        //return random integer
        int randint(int start=0, int maxnum=0, int increment=0){
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
        
        //return random double from low to high, default 0-1
        double random(double low=0, double high=1)
        {
        return low + (high - low) * rand() / ((double) RAND_MAX);
        }
        
        //return random vector shuffled
        template <class T>
        std::vector<T> shuffle(std::vector<T> v){
            std::random_shuffle(v.begin(), v.end());
            return v;
        }
};

int main(){
    Random random;
    std::vector<std::string> v = {"random", "vector", "of", "crap"};
    for (int i=0; i<3; i++)
        std::cout << random.choice(v) << " ";
    std::cout << std::endl;
    
    for (int i=0; i<3; i++)
        std::cout << random.randint(0,10) << " ";
    std::cout << std::endl;
    
    for (auto i:random.shuffle(v))
        std::cout << i << std::endl;
    
    for (auto i:v)
        std::cout << i << std::endl;

    for (int i=0; i<3; i++)
        std::cout << random.random() << " ";
    std::cout << std::endl;
}

