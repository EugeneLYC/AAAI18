#ifndef __ASG_H__
#define __ASG_H__


#include<stdlib.h>
#include<float.h>

static unsigned int ASG_size;

struct base_action {
  unsigned int *pathid_1, *pathid_2;
  float *prob_1, *prob_2;
};

struct node {
  const unsigned int id;
  struct node *next;
};

struct linkNode {
  const unsigned int id;
  struct node *header_node;
  struct base_action *node_base_action;
  struct linkNode *next;
};


struct asg_handler {
  static struct linkNode *asg_entry, *asg_tail;
  struct linkNode *init_asg(unsigned int size, struct base_action *action_entry);
  struct base_action *combination(const struct base_action *comb_base_action);
  bool isValid(const base_action *ba1, const base_action *ba2);
};

#endif /*!ASG.h */
