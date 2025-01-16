package Practice.Stack;

import java.util.EmptyStackException;

public class ListStack <E> {
    //field
    private Node<E> top;
    private int size;
    
    //construcetor
    public ListStack(){
        top = null;
        size = 0;                
    }

    //method
    public int size(){
        return  size;
    }

    public boolean isEmpty(){
        if(size()==0){return true;}
        return false;
    }

    public E peek(){
        if(isEmpty()){throw new EmptyStackException();}
        System.out.println(top.getItem());
        return top.getItem();
    }

    public void push(E newItem){
        Node newNode = new Node(newItem, top);
        top = newNode;
        size++;
        System.out.println(newItem + "is successfully added");
    }

    public E pop(){
        if(isEmpty()){throw new EmptyStackException();}
        E topItem = top.getItem();
        top = top.getNext();
        size--;
        System.out.println(topItem + "is successfully deleted");
        return topItem;
    }

    public void print(){
        Node p = top;
        if(isEmpty()){throw new EmptyStackException();}
        for(int i=0; i<size(); i++){
            System.out.print(p.getItem() + "\t ");
            p = p.getNext();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ListStack st = new ListStack();
        st.push("사과"); st.push("딸기"); st.peek(); st.push("배"); st.push("오렌지");
        st.print();
        st.pop();
        st.print();
    }

}
