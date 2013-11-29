// #if !defined( __linux__ ) //if not linux
#ifdef __linux__ 
    //linux code goes here
#elif __APPLE__
    //mac code
#elif _WIN32
    // windows code goes here
#else
    //#error Platform not supported
#endif



#include <iostream>

int main(){
    std::cout << "test" << std::endl;
}
