package Practice.Stack;

import java.util.EmptyStackException;

public class ArrayStack <E> {
    // field
    private E[] s; // 스택을 위한 배열
    private int top; // 스택의 top 항목의 배열 원소 인덱스

    // constructor
    public ArrayStack(){
        s = (E[]) new Object[1]; // 초기에 크기가 1인 배열 생성
        top = -1;
    }

    // method
    public int size(){
        return top+1;
    }

    public boolean isEmpty(){
        if(top == -1){
            return true;
        }
        return false;
    }

    public void resize(int newSize){
        Object[] t = new Object[newSize];
        for(int i=0; i<size(); i++){
            t[i] = s[i];
        }
        s = (E[]) t;
    }

    // peak(), push(), pop(), resize()

    public void push(E newItem){// push 연산
        if(size() == s.length){
            resize(2*s.length);
        }
        s[++top] = newItem;
    }

    public E pop(){
        if(isEmpty()) throw new EmptyStackException(); //underflow시 프로그램 정지
        E item = s[top];
        s[top--] = null;
        if(size() > 0 && size()==s.length/4){
            resize(s.length/2);
        }
        return item;
    }

    public E peek(){ // 스택 top 항목의 내용만을 리턴
        if(isEmpty()) throw new EmptyStackException();
        return s[top];
    }

    public void print(){
        if(isEmpty()){throw new EmptyStackException();}
        for(int i=0; i<size(); i++){
            System.out.print(s[i] + "\t ");
        }
        System.out.println();
    }

    public static void main(String[] args){
        ArrayStack st = new ArrayStack();
        st.push("사과"); st.push("딸기"); st.push("배"); st.push("오렌지"); st.push("포도");
        st.print();
        st.pop(); st.pop(); 
        st.print();

    }
}
