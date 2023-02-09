from context import bst

def test_avl_simple_insert():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5
    assert t.root.left.item is None and t.root.right.item is None

def test_avl_insert_no_rebalance():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5
    assert t.root.left.item is None and t.root.right.item is None
    t.insert(7)
    assert t.root.item == 5 and t.root.right.item == 7
    t.insert(4)
    assert t.root.item == 5 and t.root.left.item == 4 and t.root.right.item == 7

def test_avl_insert_simple_rebalance():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5 and t.root.left.item is None and t.root.right.item is None
    t.insert(6)
    assert t.root.item == 5 and t.root.right.item == 6
    t.insert(7)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 7

def test_avl_insert_complex_rebalance():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5 and t.root.left.item is None and t.root.right.item is None
    t.insert(6)
    assert t.root.item == 5 and t.root.right.item == 6
    t.insert(8)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 8
    t.insert(9)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 8 and t.root.right.right.item == 9
    t.insert(7)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 8 and t.root.right.left.item == 7 and t.root.right.right.item == 9

def test_avl_simple_delete():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5
    assert t.root.left.item is None and t.root.right.item is None
    t.delete(5)
    assert t.root.item is None

def test_avl_insert_simple_delete():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5 and t.root.left.item is None and t.root.right.item is None
    t.insert(6)
    assert t.root.item == 5 and t.root.right.item == 6
    t.insert(7)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 7
    t.delete(7)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item is None
    t.delete(6)
    assert t.root.item == 5 and t.root.left.item is None and t.root.right.item is None

def test_avl_insert_complex_delete():
    t = bst.AVLTree()
    assert t.root.item is None
    t.insert(5)
    assert t.root.item == 5 and t.root.left.item is None and t.root.right.item is None
    t.insert(6)
    assert t.root.item == 5 and t.root.right.item == 6
    t.insert(8)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 8
    t.insert(9)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 8 and t.root.right.right.item == 9
    t.insert(7)
    assert t.root.item == 6 and t.root.left.item == 5 and t.root.right.item == 8 and t.root.right.left.item == 7 and t.root.right.right.item == 9
    t.delete(6)
    assert t.root.item == 7 and t.root.left.item == 5 and t.root.right.item == 8 and t.root.right.left.item is None and t.root.right.right.item == 9