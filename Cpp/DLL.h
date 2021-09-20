#pragma once
#include <iostream>
using std::cout;
using std::ostream;
#include <string>
using std::string;
#include <vector>
using std::vector;
#include <sstream>
using std::ostringstream;
// DO NOT MODIFY
//
// Node
//
struct Node {
  string key{};
  int value{};
  Node *next = nullptr;
  Node *prev = nullptr;
  Node() = default;
  Node(string, int, Node * = nullptr, Node * = nullptr);
  bool operator==(const Node &) const;
  friend ostream &operator<<(ostream &out, const Node &n) {
    out << n.key << ":" << n.value;
    return out;
  }
};

Node::Node(string key_, int value_, Node *prev_, Node *next_) {
  key = key_;
  value = value_;
  prev = prev_;
  next = next_;
}

bool Node::operator==(const Node &n) const {
  if ((key == n.key) && (value == n.value)) {
    return true;
  } else {
    return false;
  }
}

// DO NOT MODIFY
//
// DLL
//
class DLL {
private:
  Node *head_ = nullptr;
  Node *tail_ = nullptr;
  size_t sz_ = 0;

public:
  DLL() = default;
  DLL(vector<Node>);
  DLL(const DLL &);
  DLL &operator=(DLL list);
  ~DLL();
  Node *get_head();
  Node *get_tail();
  size_t get_size();
  Node add_back(string, int);
  Node add_front(string, int);
  Node add_after(string, string, int);
  Node search(string);
  Node remove_front();
  Node remove_back();
  Node remove_key(string);
  int update_value(string, int);
  friend ostream &operator<<(ostream &out, const DLL &list) {
    auto itr = list.head_;
    ostringstream oss;
    for (; itr != nullptr; itr = itr->next) {
      oss << itr->key << ":" << itr->value << ", ";
    }
    string ans = oss.str();
    ans = ans.substr(0, ans.size() - 2);
    out << ans;
    return out;
  }
};

Node *DLL::get_head() { return head_; }
Node *DLL::get_tail() { return tail_; }
size_t DLL::get_size() { return sz_; }

DLL::~DLL() {
  while (head_)
    delete std::exchange(head_, head_->next);
}

DLL & DLL::operator =(DLL list) {
  using std::swap;
  swap(head_,list.head_);
  swap(tail_,list.tail_);
  swap(sz_,list.sz_);
  return *this;
}

DLL::DLL(const DLL &list) {
  for (Node *p = list.head_; p; p = p->next)
    add_back(p->key, p->value);
}

DLL::DLL(vector<Node> vec) {
  for (const auto &node : vec)
    add_back(node.key, node.value);
}

/* BEGIN MODIFICATION BELOW */
Node DLL::add_back(string str, int num) {
    Node* add_ftr_tail = new Node (str, num);
    if (sz_ == 0) {
        head_ = add_ftr_tail;
        tail_ = add_ftr_tail;
        sz_++;
        return *add_ftr_tail;
    } else {
        tail_ -> next = add_ftr_tail;
        add_ftr_tail -> prev = tail_;
        tail_ = add_ftr_tail;
        sz_++;
        return *tail_;
    }
}

Node DLL::add_front(string str, int num) {
    Node* add_before_head = new Node (str, num);
    if (sz_ == 0) {
        head_ = add_before_head;
        tail_ = add_before_head;
        sz_++;
        return *add_before_head;
    } else {
        head_ -> prev = add_before_head;
        add_before_head -> next = head_;
        head_ = add_before_head;
        sz_++;
        return *head_;
    }
}

Node DLL::add_after(string add_key, string str, int num) {
    if (add_key == tail_->key) {
        return add_back(str,num);
    }
    auto addafter = new Node(str,num);
    auto itr = head_;
    while (itr != tail_) {
        if (itr->key == add_key) {
            auto nextkey = itr -> next;
            itr -> next = addafter;
            nextkey -> prev = addafter;
            addafter -> next =nextkey;
            addafter -> prev = itr;
            sz_++;
            return *addafter;
        }
        itr = itr -> next;
    }
    return Node("",0);
}

Node DLL::remove_back() {
    if (sz_ == 0) {
        return Node("", 0);
    } else if (sz_ == 1) {
        Node return_ftr_remove = *tail_;
        head_=nullptr;
        tail_=nullptr;
        sz_--;
        return return_ftr_remove;
    } else {
    Node return_ftr_remove = *tail_;
    Node* remove_last = tail_;
    tail_ = tail_ -> prev;
    tail_ -> next = nullptr;
    sz_--;
    delete(remove_last);
    return return_ftr_remove;
    }
}

Node DLL::remove_front() {
    if (sz_ == 0) {
        return Node("",0);
    }
    else if (sz_==1) {
        Node return_before_remove = *head_;
        head_=nullptr;
        tail_=nullptr;
        sz_--;
        return return_before_remove;
    }else {
        Node return_before_remove = *head_;
        Node* remove_first = head_;
        head_ = head_ -> next;
        head_ -> prev = nullptr;
        sz_--;
        delete (remove_first);
        return return_before_remove;
    }
}

Node DLL::remove_key(string to_remove) {
    if (head_ == nullptr) {
        return Node("",0);
    }
    if (head_ -> key == to_remove) {
        return remove_front();
    }
    if (tail_ -> key == to_remove) {
        return remove_back();
    }
    auto itr = head_;
    while (itr !=tail_) {
        if (itr -> key == to_remove) {
            Node copy_ = *itr;
            auto store_prev = itr -> prev;
            auto store_next = itr -> next;
            store_prev -> next = store_next;
            store_next -> prev = store_prev;
            sz_--;
            delete (itr);
            return copy_;
        }
        itr = itr -> next;
    }
    return Node("",0);
}

Node DLL::search(string find_key) {
    Node* itr =head_;
    while (itr != nullptr) {
        if (itr -> key == find_key) {
            return *itr;
        }
        itr = itr -> next;
    }
    return Node("",0);
}

int DLL::update_value(string find_key, int new_value) {
    Node* itr =head_;
        while (itr != nullptr) {
         if (itr -> key == find_key) {
             itr->value = new_value;
             return new_value;
         }
         itr = itr -> next;
     }
     return -1;
}
