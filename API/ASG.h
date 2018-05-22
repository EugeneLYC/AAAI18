#ifndef __ASG_H__
#define __ASG_H__

#include<iostream>
#include<cstdlib>
#include<list>
using namespace std;

class Asg_handler {
    struct atom_action {
        unsigned int *pathid;
        float *prob;
    };

    struct base_action {
        struct atom_action *at_pos, *at_neg;
    };

    struct super_action {
        list<struct base_action> *sa;
    };

    struct node {
        unsigned int id;
        struct node *next;
        node() {id = 0; next = NULL;}
        node(const unsigned int i, struct node *n) {id = i; next = n;}
    };

    struct linkNode {
        unsigned int id;
        struct node *header_node;
        struct base_action *node_base_action;
        struct linkNode *next, *prev;

        linkNode(){header_node = NULL; node_base_action = NULL; next = NULL; prev = NULL;}
        linkNode(struct node *hn, struct node *nbc, struct linkNode *n,  struct linkNode *) {
            header_node = hn;
            node_base_action = nbc;
            next = n;
            prev = p;
        }
    };

public:
    Asg_handler();
    ~Asg_handler();
    struct linkNode *init_asg(unsigned int size, struct base_action *action_entry);
    struct base_action *combination(const struct base_action *comb_base_action);
    bool isValid(const base_action *ba1, const base_action *ba2);

private:
    struct linkNode *asg_entry, *asg_tail;
    unsigned int ASG_size;
    struct linkNode *ba2linkNode(const unsigned int new_id, struct base_action *ba);
};

#endif /*!ASG.h */
