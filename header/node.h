class Node {
public:
  int val;
  Node *prev;
  Node *next;
#ifdef NODE_CHILD
  Node *child;
#endif // NODE_CHILD
};
