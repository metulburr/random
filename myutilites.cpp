#include <iostream>

#include <cstdlib> //randint
#include <ctime> //randint
#include <vector>
#include <fstream>
#include <sstream>
#include <dirent.h>


class Utility{
        bool srand_has_exc;
    public:
        //std::string randint_insert =
        //    "\n\tExample:\n\tfor (int i=0; i<10; i++){\n"
        //    "\t    cout << util.randint(5, 25) << ' ';\n"
        //    "\t}\n";
        std::string randint_help = "int randint(int start=0, int max=0, int increment=0) \n\treturn random int from start to max by increment";// + randint_insert;

        std::string reverse_help = "string reverse(string s) \n\treturn reverse string s";
        std::string join_help = "string join(vector<string> v, string sep)\nstring join(string array[], int size, string sep) \n\tjoin vector/array into string separated by sep";
        std::string max_help = "int max(int a[], int size)\nint max(vector<int> v) \n\treturn max int from vector/array";
        std::string min_help = "int min(int a[], int size)\nint min(vector<int> v) \n\treturn min int from vector/array";
        std::string sum_help = "int sum(int a[], int size)\nint sum(vector<int> v) \n\treturn total sum from vector/array";
        std::string write_help = "void write(string filename, string data)\nvoid write(string filename, vector<string> v, string sep=\"\\n\") \n\twrite data to filename \n\twrite vector to file element on each line adding sep to end of each line";
        std::string open_help = "vector<string> open(string filename) \n\treturn string vector with each element as a line from filename";
        std::string int2str_help = "string int2str(int inter) \n\tconvert from int to string";
        std::string str2int_help = "int str2int(string str) \n\tconvert from string to int";
        std::string flo2int_help = "int flo2int(float floater) \n\tconvert from float to int";
        std::string dou2int_help = "int dou2int(double d) \n\tconvert from double to int";
        std::string cha2str_help = "string cha2str(char ch) \n\tconvert from char to string";
        std::string str2cha_help = "char str2cha(string stringer) \n\tconvert from string to char";
        std::string cha2asc_help = "int cha2asc(char ch) \n\tconvert from char to ascii number";
        std::string asc2cha_help = "char asc2cha(int num) \n\tconvert from ascii number to char";
        std::string strip_help = "string strip(const string &str, const string &whitespace = \" \\t\") \n\tstrip whitespace from left and right up until other character";
        std::string reduce_help = "string reduce(const string &str, const string &fill = \" \", const string &whitespace = \" \\t\") \n\tstrip whitespace from left and right and fill";
        std::string print_help = "template <typename T> void print(T var) \n\tprint var";
    std::string getdir_help = "int getdir (std::string dir, std::vector<std::string> &files) \n\t return vector<string> of files";


        std::vector<std::string> attr = {randint_help, reverse_help, join_help, max_help, min_help,
            sum_help, write_help, open_help, int2str_help, str2int_help, flo2int_help, dou2int_help,
            cha2str_help, str2cha_help, cha2asc_help, asc2cha_help, strip_help, reduce_help, print_help};
        std::string help(){
            std::string s;
            s += "\n";
            for (int i=0; i<attr.size(); i++){
                s += attr[i] + "\n";
            }
            return s;
        }



        Utility(){
            srand_has_exc = false;
        }

    //random
        int randint(int start=0, int maxnum=0, int increment=0){
            if (!srand_has_exc){
                std::srand(std::time(0));
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
        std::string reverse(std::string s){
            return std::string(s.rbegin(), s.rend());
        }

        //join vector into string separated by sep
        std::string join(std::vector<std::string> v, std::string sep){
            std::stringstream ss;
            for(size_t i = 0; i < v.size(); ++i){
                if(i != 0)
                    ss << sep;
                ss << v[i];
            }
            return ss.str();
        }

        //join str array into string separeted by sep
        std::string join(std::string array[], int size, std::string sep){
            std::stringstream ss;
            for(size_t i = 0; i < size; ++i){
                if(i != 0)
                    ss << sep;
                ss << array[i];
            }
            return ss.str();
        }

        //get max int from array
        int max(int a[], int size){
            int mx = a[0];
            for(int i=0; i<size; i++){
                if(mx < a[i]){
                    mx = a[i];
                }
            }
            return mx;
        }
        //get min int from array
        int min(int a[], int size){
            int mn = a[0];
            for(int i=0; i<size; i++){
                if(mn > a[i]){
                    mn = a[i];
                }
            }
            return mn;
        }
        //get sum of int array
        int sum(int a[], int size){
            int total = 0;
            for(int i=0; i<size; i++){
                total += a[i];
            }
            return total;
        }
        //get max int from vector
        int max(std::vector<int> v){
            int mx = v[0];
            for (std::vector<int>::size_type i = 0; i != v.size(); i++) {
                if(mx < v[i]){
                    mx = v[i];
                }
            }
            return mx;
        }
        //get min int from vector
        int min(std::vector<int> v){
            int mn = v[0];
            for (std::vector<int>::size_type i = 0; i != v.size(); i++) {
                if(mn > v[i]){
                    mn = v[i];
                }
            }
            return mn;
        }
        //get sum of int vector
        int sum(std::vector<int> v){
            int total = 0;
            for (std::vector<int>::size_type i = 0; i != v.size(); i++) {
                total += v[i];
            }
            return total;
        }


    //file i/o
        //write full str to file
        void write(std::string filename, std::string data){
            std::ofstream f;
            f.open(filename);
            f << data;
            f.close();
        }
        //write vector to file spaced by index, separated by sep
        void write(std::string filename, std::vector<std::string> v, std::string sep="\n"){
            std::ofstream f;
            f.open(filename);
            for (std::vector<int>::size_type i = 0; i != v.size(); i++) {
                f << v[i] << sep;
            }
            f.close();
        }
        //open file and read into vector str
        std::vector<std::string> open(std::string filename){ //get entire line
            std::string s = "";
            std::vector<std::string> v;
            std::ifstream f;
            f.open(filename);
            while(getline(f, s)){
                v.push_back(s);
            }
            f.close();
            return v;
        }


    //type conversion
        //convert from int to string
        std::string int2str(int inter){
            std::stringstream num_str;
            num_str << inter;
            return num_str.str();
        }

        //convert from string to int
        int str2int(std::string str){
            int i;
            std::stringstream ss(str);
            ss >> i;
            return i;
        }

        //convert from float to int
        int flo2int(float floater){
            int i = static_cast<int>(floater);
            return i;
        }

        //convert from double to int
        int dou2int(double d){
            int i = static_cast<int>(d);
            return i;
        }

        //ocnvert from cahr to string
        std::string cha2str(char ch){
            std::stringstream ss;
            std::string s;
            ss << ch;
            ss >> s;
            return s;
        }

        //convert from string to char
        char str2cha(std::string stringer){
            std::stringstream ss;
            char c;
            ss << stringer;
            ss >> c;
            return c;
        }

        //convert from character to ascii number
        int cha2asc(char ch){
            int i;
            i = (int)ch;
            return i;
        }

        //convert from ascii number to character
        char asc2cha(int num){
            char c;
            c = (char)num;
            return c;
        }

        std::string strip(const std::string& str,
                         const std::string& whitespace = " \t")
        {
            const auto strBegin = str.find_first_not_of(whitespace);
            if (strBegin == std::string::npos)
                return ""; // no content

            const auto strEnd = str.find_last_not_of(whitespace);
            const auto strRange = strEnd - strBegin + 1;

            return str.substr(strBegin, strRange);
        }

        std::string reduce(const std::string& str,
                           const std::string& fill = " ",
                           const std::string& whitespace = " \t")
        {
            // trim first
            auto result = strip(str, whitespace);

            // replace sub ranges
            auto beginSpace = result.find_first_of(whitespace);
            while (beginSpace != std::string::npos)
            {
                const auto endSpace = result.find_first_not_of(whitespace, beginSpace);
                const auto range = endSpace - beginSpace;

                result.replace(beginSpace, range, fill);

                const auto newStart = beginSpace + fill.length();
                beginSpace = result.find_first_of(whitespace, newStart);
            }

            return result;
        }
        template <typename T>
        void print(T var){
            std::cout << var << std::endl;
        }

    int getdir (std::string dir, std::vector<std::string> &files)
    {
        DIR *dp;
        struct dirent *dirp;
        if((dp  = opendir(dir.c_str())) == NULL) {
        std::cout << "Error(" << errno << ") opening " << dir << std::endl;
        return errno;
        }

        while ((dirp = readdir(dp)) != NULL) {
        files.push_back(std::string(dirp->d_name));
        }
        closedir(dp);
        return 0;
    }
};


void test(){
    using namespace std;

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
    cout << "sum: " << util.sum(a, 10) << endl;
    
    vector<int> v;
    for (int i=0; i<util.randint(3,10); i++){
        v.push_back(util.randint(0,100));
    }
    for (vector<int>::size_type i = 0; i != v.size(); i++) {
        cout << v[i] << ' ';
    }
    cout << endl;
    cout << "max num: " << util.max(v) << endl;
    cout << "min num: " << util.min(v) << endl;
    cout << "sum: " << util.sum(v) << endl;
    
    string name = "test.html";
    util.write(name, "some\nrandom\ndata");
    vector<string> data = util.open(name);
    for (vector<int>::size_type i = 0; i != data.size(); i++) {
        cout << data[i] << endl;
    }
    vector<string> s = {"test", "this", "right\nnow"};
    util.write(name, s);
    vector<string> data2 = util.open(name);
    for (vector<int>::size_type i = 0; i != data2.size(); i++) {
        cout << data2[i] << ' ';
    }
    cout << endl;
    
    cout << util.int2str(1024).substr(0,3) << endl;
    cout << util.str2int("24") + 1 << endl;
    cout << util.flo2int(10.1) - 5 << endl;
    cout << util.cha2str('c') + "h" << endl;
    cout << util.str2cha("s") + 'h' << endl;
    cout << util.cha2asc('c') << endl;
    cout << util.asc2cha(99) << endl;

    string foo = " too much\t \tspace\t\t\t ";
    string bar = "one\ntwo";
    cout << "[" << util.strip(foo) << "]" << endl;
    cout << "[" << util.reduce(foo) << "]" << endl;
    cout << "[" << util.reduce(foo, "-") << "]" << endl;
    cout << "[" << util.strip(bar) << "]" << endl;
    
    string jointest[] = {"join", "random", "string", "array"};
    cout << util.join(jointest, 4, ",") << endl;
    vector<string> jointest2 = {"join", "random", "string", "vector"};
    cout << util.join(jointest2, ",");
    
    std::cout << util.help() << std::endl;
    std::cout << util.strip_help << endl;
    util.print(util.strip_help + "TEST");
    util.print(1 + 1.1);
    
    std::string dir = std::string(".");
    std::vector<std::string> files = std::vector<std::string>();
    util.getdir(dir,files);
    for (int i = 0;i < files.size();i++) {
        std::cout << files[i] << std::endl;
    }
}




int main (){
    test();
}
