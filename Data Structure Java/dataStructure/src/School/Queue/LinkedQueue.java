package Queue;

public class LinkedQueue <E>{
    private Node<E> tail;

    public LinkedQueue(){
        tail = null;
    }

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
        if(isEmpty()){//원소가 없을 때
            return null;
        } else {
            Node<E> front = tail.next;
            if(front == tail){//원소가 하나일 때
                tail = null;
            } else {// 원소가 2개 이상일 때
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