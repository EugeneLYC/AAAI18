#include<iostream>
#include<cstdlib>
#include<ASG.h>
#include<list>
using namespace std;

/*
 * ba2linkNode transits a base_action to a linkNode
*/
struct linkNode *
Asg_handler::ba2linkNode(const unsigned int new_id, struct base_action *ba) {
    struct linkNode *link_node = new linkNode;
    link_node->id = new_id;
    link_node->header_node = NULL;
    link_node->node_base_action = ba;
    link_node->next = NULL;
    return link_node;
}

Asg_handler::Asg_handler(const unsigned int ps = 0) {
    asg_entry = asg_tail = NULL;
    ASG_size = 0;
    PATH_size = ps;
}

struct linkNode *
Asg_handler::init_asg(unsigned int size, struct base_action *action_entry) {
    struct base_action *ba = action_entry;
    for (int i = 0; i < size; i++) {
        struct linkNode *curr_node = ba2linkNode(ASG_size, ba);
        if (ASG_size == 0) {
            asg_entry = asg_tail = curr_node;
        }
        else {
            curr_node->next = asg_entry;
            curr_node->prev = asg_tail;
            asg_tail->next = curr_node;
            asg_tail = curr_node;
        }
        ASG_size++;
        ba++;
    }

    curr_node = asg_entry;
    struct linkNode *itr = asg_entry;
    struct node *neighbor_ptr = curr_node->header_node;
    for (int i = 0; i < ASG_size; i++) {
        for (int j = 0; j < ASG_size; j++) {
            if (itr == curr_node) {
                continue;
            }
            if (isValid(itr, curr_node)) {
                struct node *neighbor = new node(itr->id);
                neighbor_ptr->next = neighbor;
                neighbor_ptr = neighbor;
            }
        }
    }
    return asg_entry;
}

bool
Asg_handler::isValid(const base_action *ba1, const base_action *ba2) {
    if (ba1->at_pos->pathid == ba2->at_neg->pathid || ba2->at_pos->pathid == ba1->at_neg->pathid) {
        return false;
    }
    if (ba1->at_pos->pathid == ba2->at_pos->pathid && ba1->at_pos->prob + ba2->at_pos->prob > 1) {
        return false;
    }
    if (ba1->at_neg->pathid == ba2->at_neg->pathid && ba1->at_neg->prob + ba2->at_neg->prob < -1) {
        return false;
    }
    return true;
}
