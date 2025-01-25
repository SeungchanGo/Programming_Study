package Queue;

public class Node<E> {
    public E item;
    public Node<E> next;

    public Node(E newItem, Node<E> nextNode){
        item = newItem;
        next = nextNode;
    }

    public Node(E newItem){
        item = newItem;
        next = null;
    }
    
}
