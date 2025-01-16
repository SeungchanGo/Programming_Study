package Practice.Queue;

import java.util.NoSuchElementException;

public class ArrayQueue <E> {
    //field
    private E[] q; // 큐를 위한 배열
    private int size, front, rear; 

    //constructor
    public ArrayQueue(){
        q = (E[]) new Object[2]; //초기에 크기가 2인 배열 생성
        front = rear = size = 0;
    }

    //method
    public int size(){
        return size;
    }

    public boolean isEmpty(){
        if(size()==0){return true;}
        return false;
    }

    // rear 다음의 비어있는 원소의 인덱스는 rear = (rear+1) % N (N = 배열의 크기)

    public void resize(int newSize){
        Object[] t = new Object[newSize];
        for(int i=1, j=front+1; i<size+1; i++, j++){
            t[i] = q[j%q.length]; // 배열 q의 항목들을 t[1]에서부터 복붙
        }
        front = 0;
        rear = size;
        q = (E[]) t; // 배열 t를 배열 q로

    }

    public void add(E newItem){
        if((rear+1)%q.length == front){ //비어있는 배열이 1개인 경우, 즉 큐가 full인 경우
            resize(2*q.length);
        }
        rear = (rear+1)%q.length;
        q[rear] = newItem;
        size++;
    }

    public E remove(){
        if(isEmpty()){throw new NoSuchElementException();}
        front = (front+1)%q.length;
        E frontItem = q[front];
        q[front] = null;
        size--;
        if(size > 0 && size == q.length/4){
            resize(q.length/2);
        } 
        return frontItem;
    }

    public void print1(){
        if(isEmpty()){throw new NoSuchElementException();}
        for(int i=0; i<q.length; i++){
            System.out.print(q[i] + "\t ");
        }
        System.out.println();
    }


    public void print2(){
        if(isEmpty()){throw new NoSuchElementException();}
        Object[] x = new Object[size];
        for(int i=1, j= front+1; i<size+1; i++, j++){
                x[i] = q[j%q.length];
                System.out.print(x[i]+ "\t ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ArrayQueue aq = new ArrayQueue();
        aq.add("딸기"); aq.add("배"); aq.add("사과"); aq.add("포도"); aq.add("망고");
        aq.print1();
        aq.remove();
        aq.print1();
        aq.remove();
        aq.print1();
        aq.add("바나나");
        aq.print1();
    }

}
