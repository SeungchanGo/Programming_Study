package Deque;

public class ArrayDeque<E> implements DequeInterface<E>{
    //field
    private E[] queue;
    private int numItems, front, tail;
    private static final int DEFAULT_NUM = 10;

    //constructor
    public ArrayDeque(){
        queue = (E[]) new Object[DEFAULT_NUM];
        numItems = front = tail = 0;
    }

    public ArrayDeque(int size){
        queue = (E[]) new Object[size];
        numItems = front = tail = 0;
    }

    //method
    @Override
    public String toString() {
        String str = "[";
        if(front<tail){
            for(int i=front+1; i<=tail; i++){
                str += queue[i];
                if(i<tail){
                    str += ",";
                }
            }
        } else {
            for(int i=front+1; i<=queue.length-1; i++){
                str += queue[i] + ",";
            }
            for(int i=0; i<=tail; i++){
                str += queue[i];
                if(i<tail){
                    str+=",";
                }
            }
        }
        str += "]";
        return str;  
    }

    @Override
    public void insertFront(E x) {
        if(isFull()){
            System.out.println("Deque is full");
        } else {
            queue[front] = x;
            front = (front-1+queue.length) % queue.length;
            numItems++;
        }
    }

    @Override
    public void insertLast(E x) {
        if(isFull()){
            System.out.println("Deque is full");
        } else {
            tail = (tail+1) % queue.length;
            queue[tail] = x;
            numItems++;
        } 
    }

    @Override
    public E deleteFront() {
        if(isEmpty()){
            return null;
        } else {
            front = (front+1) % queue.length;
            E item = queue[front];
            queue[front] = null;
            numItems--;
            return item;
        }
    }

    @Override
    public E deleteLast() {
        if(isEmpty()){
            return null;
        } else {
            E item = queue[tail];
            queue[tail] = null;
            tail = (tail-1+queue.length) % queue.length;
            numItems--;
            return item;
        }   
    }

    @Override
    public E getFront() {
        if(isEmpty()){
            return null;
        } else {
            return queue[(front+1)%queue.length];
        } 
    }

    @Override
    public E getLast() {
        if(isEmpty()){
            return null;
        } else {
            return queue[tail];
        }   
    }

    @Override
    public boolean isEmpty() {
        return numItems == 0;
    }

    public boolean isFull(){
        return numItems == queue.length;
    }

    @Override
    public void dequeAll() {
       queue = (E[]) new Object[queue.length];
       front = tail = numItems = 0; 
        
    }

}