package Practice.List;

public class Node <E> {
    //field
    private E item;
    private Node next;

    //constructor
    public Node(E newItem, Node p){
        item = newItem;
        next = p;
    }

    //method
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
