#include<iostream>
using namespace std;

class Blag {
private:
    struct ASG *actionSetGraph;
    struct list list_of_neighbor;
    char *msg_buffer;
public:
    Blag();
    ~Blag();
    void init_asg();
    char *recv_command();
};
