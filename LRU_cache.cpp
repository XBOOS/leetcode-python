/*
 * Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
 *
 * get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
 * set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
 *
 *
 */

class LRUCache{

public:
    //inner class for node of linkedHashMap.
    class Node{
    public:
        int key;
        int val;
        Node* pre;
        Node* next;
        Node(){}
        Node(int key,int val){
            this->key = key;
            this->val = val;
            this->pre = nullptr;
            this->next = nullptr;
        }
    };

    Node* head;
    Node* tail;
    map<int,Node*> nodeMap;
    int capacity;

    LRUCache(int capacity) {
        this->capacity = capacity;
        this->head = new Node(0,0);
        this->tail = new Node(0,0);
        this->head->next = tail;
        this->tail->pre = head;
    }

    int get(int key) {
        map<int,Node*>::iterator it = nodeMap.find(key);
        if(it!=nodeMap.end()){
            //update the frequency by moving it to end of the linked-list
            Node* node = it->second;
            //delete and insert
            node->pre->next = node->next;
            node->next->pre = node->pre;
            appendTail(node);
            return node->val;
        }else{
            return -1;
        }
    }
    void appendTail(Node* node){
        tail->pre->next = node;
        node->next = tail;
        node->pre = tail->pre;
        tail->pre = node;
    }
    void set(int key, int value) {
        map<int,Node*>::iterator it = nodeMap.find(key);
        if(it!=nodeMap.end()){//the key exists, update the value and
            //update the frequency by moving it to end of the linked-list
            Node* node = it->second;
            node->val = value;

            //delete and insert
            node->pre->next = node->next;
            node->next->pre = node->pre;
            appendTail(node);
        }else{
            //doesnt exists now , check capacity first
            if(nodeMap.size()==this->capacity){
                int tmp = this->head->next->key;
                this->head->next = this->head->next->next;
                this->head->next->pre  = this->head;
                //printf("1-----%d",nodeMap.size());
                this->nodeMap.erase(tmp);//used wrong key here
                //printf("2-----%d",nodeMap.size());

            }

                Node* ptr =new Node(key,value);
                nodeMap.insert(std::pair<int,Node*>(key,ptr));
                appendTail(ptr);

        }
    }
};

/*set size one of the field*/
class LRUCache{

public:
    //inner class for node of linkedHashMap.
    class Node{
    public:
        int key;
        int val;
        Node* pre;
        Node* next;
        Node(){}
        Node(int key,int val){
            this->key = key;
            this->val = val;
            this->pre = nullptr;
            this->next = nullptr;
        }
    };

    Node* head;
    Node* tail;
    map<int,Node*> nodeMap;
    int capacity;
    int size;

    LRUCache(int capacity) {
        this->capacity = capacity;
        this->size = 0;
        this->head = new Node(0,0);
        this->tail = new Node(0,0);
        this->head->next = tail;
        this->tail->pre = head;
    }

    int get(int key) {
        map<int,Node*>::iterator it = nodeMap.find(key);
        if(it!=nodeMap.end()){
            //update the frequency by moving it to end of the linked-list
            Node* node = it->second;
            //delete and insert
            node->pre->next = node->next;
            node->next->pre = node->pre;
            appendTail(node);
            return node->val;
        }else{
            return -1;
        }
    }
    void appendTail(Node* node){
        tail->pre->next = node;
        node->next = tail;
        node->pre = tail->pre;
        tail->pre = node;
    }
    void set(int key, int value) {
        map<int,Node*>::iterator it = nodeMap.find(key);
        if(it!=nodeMap.end()){//the key exists, update the value and
            //update the frequency by moving it to end of the linked-list
            Node* node = it->second;
            node->val = value;

            //delete and insert
            node->pre->next = node->next;
            node->next->pre = node->pre;
            appendTail(node);
        }else{
            //doesnt exists now , check capacity first
            if(nodeMap.size()==this->capacity){
                int tmp = this->head->next->key;
                this->head->next = this->head->next->next;
                this->head->next->pre  = this->head;
                //printf("1-----%d",nodeMap.size());
                this->nodeMap.erase(tmp);//used wrong key here
                //printf("2-----%d",nodeMap.size());
                this->size--;
            }

                Node* ptr =new Node(key,value);
                nodeMap.insert(std::pair<int,Node*>(key,ptr));
                appendTail(ptr);
                this->size++;

        }
    }
};
