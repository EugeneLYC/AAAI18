#include <stdio.h>
#include <stdlib.h>
#include "list.h"
struct fox{
    unsigned int weight;
    int is_cute;
    struct list_head list;
};
int main()
{
    struct fox *red_fox;
    red_fox=(struct fox*)malloc(sizeof(struct fox));
    red_fox->weight=6;
    red_fox->is_cute=0;
    INIT_LIST_HEAD(&red_fox->list);
    printf("red_fox:\t%p\t%p\t%p\n",&red_fox->list,
                         (red_fox->list).next,
                         (red_fox->list).prev);

    printf("\t\t%p\t%d\t%d\n",&red_fox->list, red_fox->weight, red_fox->is_cute);

    struct fox *write_fox;
    write_fox=(struct fox*)malloc(sizeof(struct fox));
    write_fox->weight=7;
    write_fox->is_cute=-1;
    INIT_LIST_HEAD(&write_fox->list);
    printf("write_fox:\t%p\t%p\t%p\n",&write_fox->list,
                         (write_fox->list).next,
                         (write_fox->list).prev);

    printf("\t\t%p\t%d\t%d\n",&write_fox->list, write_fox->weight, write_fox->is_cute);
    //链表头
    LIST_HEAD(fox_list);
    //添加
    list_add(&(red_fox->list),&fox_list);
    list_add(&(write_fox->list),&fox_list);

    struct fox *pos;
    //遍历
    list_for_each_entry(pos,&fox_list,list){
        printf("%p\t%d\t%d\n",&pos->list, pos->weight, pos->is_cute);
    }
    //删除
    list_del(&(red_fox->list));
    free(red_fox);
    list_del(&(write_fox->list));
    free(write_fox);
    list_for_each_entry(pos,&fox_list,list){
        printf("%p\t%d\t%d\n",&pos->list, pos->weight, pos->is_cute);
    }
    return 0;
}
