package Practice.Stack;

public class Node <E> {
    private E item;
    private Node next;

    public Node(E newItem, Node p){
        item = newItem;
        next = p;
    }

    public E getItem(){
        return item;
    }

    public Node getNext(){
        return next;
    }

    public void setItem(E newItem){
        item = newItem;
    }

    public void setNext(Node p){
        next = p;
    }
    
}
