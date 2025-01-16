package Practice;

public class Node <E>{
    //field
    public E item;
    public Node<E> next;

    //public 
    public Node(E newItem, Node<E> nextNode){
        item = newItem;
        next = nextNode;
    }

    
}
