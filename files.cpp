
#include <iostream>
#include <fstream>
#include <vector>

class File{
    public:
        std::vector<std::string> tokens;
        
        friend std::ostream& operator<<(std::ostream& stdout, const File& obj);
    
        void write(std::string filename, std::string sep="\n"){
            std::ofstream f;
            f.open(filename);
            for (std::vector<int>::size_type i = 0; i != this->tokens.size(); i++) {
                f << this->tokens[i] << sep;
            }
            f.close();
        }

        void open(std::string filename){
            std::string s = "";
            std::ifstream f;
            f.open(filename);
            while(getline(f, s)){
                this->tokens.push_back(s);
            }
            f.close();
        }

};

std::ostream& operator<<(std::ostream& stdout, const File& obj){
    std::string start = "[", end = "]", delim = ", ";
    std::string s;
    if (obj.tokens.size() > 0){
        s += start;
        for (auto i: obj.tokens){
            s += i;
            if (i != obj.tokens.back()){
                s += delim;
            }
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
    File file;
    file.open("save.txt");
    std::cout << file;
    
}
