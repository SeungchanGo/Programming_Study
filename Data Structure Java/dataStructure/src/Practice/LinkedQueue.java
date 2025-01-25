package Practice;

public class LinkedQueue <E>{
    //field
    private Node<E> tail;

    //constructor
    public LinkedQueue(){
        tail = null;
    }

    //method
    public void enqueue(E newItem){
        Node<E> newNode = new Node<E>(newItem, null);
        if(isEmpty()){
            newNode.next = newNode;
            tail = newNode;
        } else {
            newNode.next = tail.next;
            tail.next = newNode;
            tail = newNode;
        }
    }

    public E dequeue(){
        if(isEmpty()){
            return null;
        } else {
            Node<E> front = tail.next;
            if(front == tail){
                tail = null;
            } else {
                tail.next = front.next;
            }
            return front.item;
        }
    }

    public E front(){
        if(isEmpty()){
            return null;
        } else {
            return tail.next.item;
        }
    }

    public boolean isEmpty(){
        return tail == null;
    }

    public void dequeueAll(){
        tail = null;
    }
}

