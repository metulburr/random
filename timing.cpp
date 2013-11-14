#include <iostream>
#include <ctime>

class Time{
    public:
        clock_t start_, end_;
        double sec;
        int start_num = 0;
        bool stop_flag = false;
        
        
        Time(int start_at) : start_num(start_at){

        }
        Time(){

        }
        void start(){
            stop_flag = false;
            time(&start_);
        }
        void restart(){
            stop_flag = false;
        }
        void end(){
            time(&end_);
        }
        void stop(){
            stop_flag = true;
        }
        double seconds(){
            if (! stop_flag){
                end();
            }
            double sec = difftime(end_,start_) + start_num;
            return sec;
        }
};

int main(){
    Time timer;
    timer.start();
    while(true){
        double num = timer.seconds();
        std::cout << num << std::endl;
        if (num == 4){
            timer.stop();
            timer.restart();
        }

        
    }
}
