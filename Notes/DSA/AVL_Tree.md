## AVL Tree

An AVL Tree also known as the self-balancing tree, where the difference between heights of left and right subtrees for any node cannot be more than one.

- Rotations: rotations are designed to restore balance in O(1) time while ensuring the overall time complexity remains O(log n). AVL Trees use four cases to rebalance themselves after insertions and deletions: Left-Left (LL), Right-Right (RR), Left-Right (LR) and Right-Left (RL)

- Insertion and Deletion: While insertion is followed by upward traversals to check balance and apply rotations, deletion can be more complex due to multiple rotations possibly being required. AVL Trees may require multiple rebalancing steps during deletion, unlike Red-Black Trees which limit this better.

- Use Cases: AVL Trees are particularly useful when you need frequent and efficient lookups, like in database indexing, memory-intensive applications, or where predictable time complexity is crucial.

- Drawbacks Compared to Other Trees: Although faster in lookups than Red-Black Trees, AVL Trees might incur slightly more overhead on insertions and deletions due to stricter balancing requirements. As a result, Red-Black Trees are more common in standard libraries like TreeMap or TreeSet in Java or map in C++ STL.

- In-order Traversal: An in-order traversal of an AVL Tree still gives you elements in sorted order, just like any Binary Search Tree.


