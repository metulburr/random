
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

std::string replace(std::string s, const std::string& find, const std::string& replacement) {
    size_t pos = 0;
    while ((pos = s.find(find, pos)) != std::string::npos) {
        s.replace(pos, find.length(), replacement);
        pos += replacement.length();
    }
    return s;
}

std::ostream& operator<<(std::ostream& stdout, const File& obj){
    std::string start = "[", end = "]", delim = "\', \'";
    std::string s;
    if (obj.tokens.size() > 0){
        s += start + "\'";
        for(auto it = obj.tokens.begin(); it != obj.tokens.end(); ++it){
            s += *it;
            if (&*it != &obj.tokens.back()){ //if addresss of iterator is not address of last element
                s += delim;
            }
        }
        s += "\'" + end;
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
    file.tokens.push_back(" ");
    file.save();
    file.load();
    std::cout << file << std::endl;

    
}
