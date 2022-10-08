#include <iostream>
using namespace std;

struct Node{
    int data;
    struct Node * link;
}*start;

void create_list(int data){
    struct Node *q, *temp;
    temp = (struct Node*) malloc(sizeof(struct Node));
    temp->data= data;
    temp->link=NULL;
    q= start;
    if(q==NULL){
        start= temp;
        return;
    }
    while(q->link!=NULL){
        q=q->link;
    }
    q->link= temp;
    q=q->link;
    q=temp;
}

void add_at_beginning(int data){
    struct Node *temp;
    temp= (struct Node *) malloc(sizeof(struct Node));
    temp->data= data;
    temp->link= start;
    start=temp;
}

void add_after(int data, int pos){
    struct Node *temp, *q;
    temp= (struct Node *) malloc(sizeof(struct Node));
    temp->data= data;
    temp->link=NULL;
    q= start;
    for(int i=0;i<pos;i++){
        q=q->link;
        if(q==NULL){
            cout<<("No index found to insert element");
            return;
        }
    }
    temp->link= q->link;
    q->link= temp;
}

void del(int data){
    struct Node *temp, *q;
    if(start->data== data){
        temp=start;
        start=start->link;
        free(temp);
        return;
    }
    q= start;
    while(q->link!=NULL){
        if(q->link->data==data){
            temp= q->link;
            q->link= temp->link;
            free(temp);
            return;
        }
        q=q->link;
    }
}

void display(){
    struct Node *q;
    q= start;
    if(q==NULL){
        cout<<"List is empty";
        return;
    }
    while(q!=NULL){
        cout<<q->data<<" ";
        q=q->link;
    }
}

void count(){
    struct Node *q;
    q=start;
    int count= 0;
    while(q!=NULL){
        q=q->link;
        count++;
    }
    cout<<"Number of element in the linked list= "<<count<<endl;
}

void search(int data){
    struct Node *q;
    q=start;
    int pos=0;
    while(q!=NULL){
        if(q->data==data){
            cout<<"Found at index- "<<pos<<endl;
        }
        pos++;
        q=q->link;
    }
}

void rev(){
    struct Node *p1, *p2, *p3;
    if(start->link==NULL){
        return;
    }
    p1= start;
    p2= p1->link;
    p3= p2->link;
    p1->link=NULL;
    p2->link= p1;
    while(p3!=NULL){//More than three elements
        p1=p2;
        p2=p3;
        p3=p3->link;
        p2->link= p1;
    }
    start=p2;
}

int main(){
    create_list(2);
    create_list(1);
    create_list(5);
    create_list(7);
    display();
    del(1);
    cout<<"\n";
    display();

    
}