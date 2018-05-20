#include<iostream>
using namespace std;

struct node {
    int id;
    struct node *next;
};

struct linkNode {
    struct linkNode *next, *prev;
    struct node *header;
};

struct ASG {
    linkNode *asg;
};


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
