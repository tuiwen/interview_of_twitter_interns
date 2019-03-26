// gcc mkdate.cpp -o mkdate -std=c++11 -Wall -lstdc++
#include <cstdint>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <random>

using namespace std;

int main(int argc, const char *argv[]) {
    if(argc != 2) {
        cout << "usage:\n\tmkdate <interger>\n" << endl;
        exit(1);
    }
    int64_t cnt = 0;
    int64_t wall = atoll(argv[1]);
    if(wall <= 0 && wall >= ((int64_t)2 >> 32)) {
        cout << "error: input must be a positive integer\n" << endl;
        exit(1);
    }
    wall *= 10000;
    mt19937 mt_rand(time((time_t *)NULL));
    char buf[1024];
    while(cnt < wall) {
        int n = sprintf(buf, "%u-%u-%u %u:%u:%u",
                        mt_rand() % 20 + 2000,
                        mt_rand() % 12 + 1,
                        mt_rand() % 31 + 1,
                        mt_rand() % 24 + 1,
                        mt_rand() % 60 + 1,
                        mt_rand() % 60 + 1);
        buf[n] = '\0';
        cout << buf << endl;
        cnt++;
    }
    return 0;
}
