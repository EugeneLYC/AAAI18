#include<assert.h>
#include<stdlib.h>
#include<float.h>
#include<ASG.h>

extern static unsigned int ASG_size;
extern static struct linkNode *asg_entry, *asg_tail;

struct base_action *
init_base_action(unsigned int *id1, unsigned int *id2, float *prob1, float *prob2) {
  struct base_action *ba;
  ba->pathid_1 = id1;
  ba->pathid_2 = id2;
  ba->prob_1 = prob1;
  ba->prob_2 = prob2;
  return ba;
}

bool
destruct(struct base_action *ba) {
  assert(ba != NULL);
  ba->pathid_1 = NULL;
  ba->pathid_2 = NULL;
  ba->prob_1 = NULL;
  ba->prob_2 = NULL;
  return true;
}

struct linkNode *
ba2linkNode(const unsigned int new_id, struct base_action *ba) {
  struct linkNode *link_node;
  link_node->id = new_id;
  link_node->header_node = NULL;
  link_node->node_base_action = ba;
  link_node->next = NULL;
  return link_node;
}

struct linkNode *
init_asg(unsigned int size, struct base_action *action_entry) {
  ASG_size = 0;
  asg_entry = asg_tail = NULL;

  struct base_action *ba = action_entry;
  for (int i = 0; i < size; i++) {
    struct linkNode *link_node = ba2linkNode(ASG_size, ba);
    if (ASG_size == 0) {
      asg_entry = link_node;
      asg_tail = link_node;
    }
    else {
      asg_tail->next = link_node;
      asg_tail = link_node;
    }
    ASG_size++;
    ba++;
  }
  return asg_entry;
}

bool
isValid(const base_action *ba1, const base_action *ba2) {
  if ((ba1->pathid_1 == ba2->pathid_1) || (ba1->pathid_2 == ba2->pathid_2)) {
    if (ba1->prob_1 * ba2->prob_1 < 0 || ba1->prob_2 * ba2->prob_2 < 0) {
      return false;
    }
  }
  else {
    if (ba1->prob_1 + ba2->prob_1 > 1 || ba1->prob_1 + ba2->prob_1 < 0 || \
      ba1->prob_2 + ba2->prob_2 > 1 || ba1->prob_2 + ba2->prob_2 < 0) {
      return false;
    }
  }
  return true;
}
