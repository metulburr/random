#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <iomanip>

template <class KEY, class VALUE>
class Dict{
    public:
        std::map<KEY, VALUE> dictionary;
        
        void update(KEY k, VALUE v){
            dictionary[k] = v;
        }
        
        std::vector<KEY> keys(){
            std::vector<KEY> v;
            for(class std::map<KEY, VALUE>::const_iterator it = dictionary.begin();
            it != dictionary.end(); ++it){
                v.push_back(it->first);
            }
            return v;
        }
        
        std::vector<VALUE> values(){
            std::vector<VALUE> v;
            for(class std::map<KEY, VALUE>::const_iterator it = dictionary.begin();
            it != dictionary.end(); ++it){
                v.push_back(it->second);
            }
            return v;
        }
};

int main(){
    Dict<std::string, std::string> d;
    d.update("key", "value");
    d.update("key2", "value2");
    
    for (auto i:d.keys())
        std::cout << i << std::endl;
        
    for (auto i:d.values())
        std::cout << i << std::endl;
}
