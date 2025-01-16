package Practice;

public class ArrayDeq <E> {
    //field
    private E[] deq;
    private int numItems, front, tail;
    private static final int DEFAULT_NUM = 10;

    //constructor
    public ArrayDeq(){
        deq = (E[]) new Object[DEFAULT_NUM];
        numItems = front = tail = 0;
    }

    //method
    public void insertFront(E newItem){
        if(deq.length == numItems){
            System.out.println("Deq is fulled"); 
        } else {
            deq[front] = newItem;
            front = (front-1+deq.length)%deq.length;
            numItems++;
        }
    }

    public void insertLast(E newItem){
        if(deq.length == numItems){
            System.out.println("Deq is fulled");
        } else {
            tail = (tail+1)%deq.length;
            deq[tail] = newItem;
            numItems++;
        }
    }

    public E deleteFront(){
        if(isEmpty()){
            return null;
        } else {
            front = (front+1) % deq.length;
            E rItem = deq[front];
            deq[front] = null;
            numItems--;
            return rItem;
        }
    }

    public E deleteLast(){
        if(isEmpty()){
            return null;
        } else {
            E rItem = deq[tail];
            deq[tail] = null;
            tail = (tail-1+deq.length)%deq.length;
            numItems--;
            return rItem;
        }
    }

    public E front(){
        if(isEmpty()){
            return null;
        } else {
            return deq[(front+1)%deq.length];
        }
    }

    public E Last(){
        if(isEmpty()){
            return null;
        } else {
            return deq[tail];
        }
    }

    public boolean isEmpty(){
        return numItems == 0;
    }

    public void deleteAll(){
        deq = (E[]) new Object[deq.length];
        numItems = front = tail = 0;
    }
    
}
