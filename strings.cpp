
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>


class String{
    public:
        std::string str;
        std::vector<std::string> tokens;
        char delim;
    
        String(std::string string, char delimiter='\n'){
            str = string;
            delim = delimiter;
            tokens = split();
        }
        
        std::string 
        operator*(int num){
            std::string s;
            for (int i=0; i<num; i++){
                s += this->str;
            }
            return s;
        }
        
        bool 
        startswith(std::string search){
            if ( this->str.compare(0, search.length(), search) == 0)
                return true;
            else
                return false;
        }
        bool 
        endswith(std::string search){
            if (search.length() > str.length())
                return false;
            int len = str.length();
            int start = str.length() - search.length();
            if ( this->str.compare(start, len, search) == 0)
                return true;
            else
                return false;
        }
        
        //split self.str into vector
        std::vector<std::string> 
        split(){
            std::vector<std::string> v;
            std::stringstream ss(this->str);
            std::string temp;
            while( getline(ss, temp, this->delim)){
                v.push_back(temp);
            }
            return v;
        }
        
        //join vector of elements to one string by sep
        template <class T> std::string 
        join(const std::vector<T> &v, std::string sep="\n"){
            std::string s;
            for (auto i:v){
                s += i;
                s += sep;
            }
            return s;
        }
        
        std::string 
        upper(){
            std::string s = this->str;
            std::transform(s.begin(), s.end(), s.begin(), toupper);
            return s;
        }

        std::string 
        lower(){
            std::string s = this->str;
            std::transform(s.begin(), s.end(), s.begin(), tolower);
            return s;
        }

        std::string 
        replace(const std::string& find, const std::string& replacement) {
            std::string s = this->str;
            size_t pos = 0;
            while ((pos = s.find(find, pos)) != std::string::npos) {
                s.replace(pos, find.length(), replacement);
                pos += replacement.length();
            }
            return s;
        }
        
        std::string 
        strip(const std::string &whitespace = " \t\n"){
            std::string s = this->str;
            const auto start = s.find_first_not_of(whitespace);
            const auto end = s.find_last_not_of(whitespace);
            const auto range = end - start + 1;
            
            if (start == std::string::npos)
                return ""; // no content
            else
                return s.substr(start, range);
        }
        
        //if constructor arg is only a number, return true if between start and end, else false
        template <class T, class U> bool 
        between(T start, U end){
            double number;
            std::stringstream ss(this->str);
            ss >> number;
            
            if (number > start && number < end)
                return true;
            else
                return false;
        }
        
        std::string 
        splice(std::string s, int front=0, int back=0){
            std::string s2 = s.substr(front);
            std::string s3 = std::string(s2.rbegin(), s2.rend()).substr(back);
            return std::string(s3.rbegin(), s3.rend());
        }
                
        
        
};


//convert std::string to char*
class DeepString{
        DeepString(const DeepString& other);
        DeepString& operator=(const DeepString& other);
        char* internal_; 
    public:
        explicit DeepString( const std::string& toCopy): 
            internal_(new char[toCopy.size()+1]) 
        {
            std::strcpy(internal_,toCopy.c_str());
        }
        ~DeepString(){ 
            delete[] internal_; 
        }
        char* str() const{ 
            return internal_;
        }
        const char* c_str()  const{
            return internal_;
        }
};



int main(){
    
    DeepString deep("SDL_VIDEO_CENTERED=1");
    putenv(deep.str());
    
    
    
    const char *file =
        "print \"HI\"\n"
        "nline\n"
        "print ( 2 + 2 )\n"
        "end\n";
    
    String filer(file, '\n');
    std::vector<std::string> v = filer.split();

    for (auto i:v){
        String line(i, ' '); //split line by spaces

        if (line.tokens[0] == "print"){
            std::cout << "-> ";
        }
        else if (line.str == "end"){
            std::cout << "<- ";
        }
        std::cout << i << " (" << line.tokens.size() << ")" << std::endl;
    }
    
    String num("9.2");
    std::cout << num.between(9.1, 20) << std::endl;

}
