
#include <iostream>
#include <fstream>
#include <vector>

class File{
    public:
        std::vector<std::string> tokens;
        std::string filename;
        
        File(std::string name) : filename(name){
            
        }

        
        friend std::ostream& operator<<(std::ostream& stdout, const File& obj);
    
        void save(std::string sep="\n"){
            std::ofstream f;
            f.open(this->filename);
            for (std::vector<int>::size_type i = 0; i != this->tokens.size(); i++) {
                f << this->tokens[i] << sep;
            }
            f.close();
        }

        void load(){
            this->tokens.clear();
            std::string s;
            std::ifstream f;
            f.open(this->filename);
            while(getline(f, s)){
                this->tokens.push_back(s);
            }
            f.close();
        }

};

std::ostream& operator<<(std::ostream& stdout, const File& obj){
    std::string start = "[", end = "]", delim = "\", \"";
    std::string s;
    if (obj.tokens.size() > 0){
        s += start;
         s += "\"";
        for(auto it = obj.tokens.begin(); it != obj.tokens.end(); ++it){
            s += *it;
            if (&*it != &obj.tokens.back()){ //if addresss of iterator is not address of last element
                s += delim;
            }
            else
                s += "\"";
        }
        s += end;
    }
    else{
        s += start;
        s += end;
    }
    stdout << s;
    return stdout;
}

int main(){
    File file("save.txt");
    file.load();
    std::cout << file << std::endl;
    file.tokens.push_back("t");
    file.save();
    file.load();
    std::cout << file << std::endl;

    
}
