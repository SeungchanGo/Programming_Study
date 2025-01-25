package Deque;

public interface DequeInterface<E> {
    public void insertFront(E x);
    public void insertLast(E x);
    public E deleteFront();
    public E deleteLast();
    public E getLast();
    public E getFront();
    public boolean isEmpty();
    public void dequeAll();


}
