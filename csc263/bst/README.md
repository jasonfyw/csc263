# Binary Search Trees

BSTs are binary trees where the root of a subtree is greater than all the nodes in the left subtree and smaller than all the nodes in the right subtree.

For a BST with height $h$:
- `search(x)`: $WC\in\mathcal{O}(h)\in\mathcal{O}(n)$
- `insert(x)`: $WC\in\mathcal{O}(h)\in\mathcal{O}(n)$
- `delete(x)`: $WC\in\mathcal{O}(h)\in\mathcal{O}(n)$

## AVL Trees

Adelson-Velsky and Landis (AVL) Trees are self-balancing trees. They aim to keep the height on the order of $\log n$ by maintaining a balancing condition.

**Balancing condition**: for each node, the heights of the subtrees differ by at most 1.

This balancing condition is maintained by performing **rotations** – mechanisms to rebalance an overly tall subtree by reducing its height by 1.


*Note:* tree height is the number of vertices along the longest path from a leaf to the root. Here, an empty tree has height -1 and a tree with one node has height 0.

For an AVL tree with height $h$:
- `search(x)`: $WC\in\mathcal{O}(h)\in\mathcal{O}(\log n)$
- `insert(x)`: $WC\in\mathcal{O}(h)\in\mathcal{O}(\log n)$
- `delete(x)`: $WC\in\mathcal{O}(h)\in\mathcal{O}(\log n)$

