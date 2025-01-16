package Practice.List;

import java.util.NoSuchElementException;
public class ArrList <E>{
    //field
    private E[] a; //리스트 항목들의 저장할 배열
    private int size; // 리스트의 항목 수

    //constructor
    public ArrList(){
        a = (E[])new Object[1]; // 최초로 1개의 원소를 가진 배열 생성
        size = 0; // 항목 수를 0으로 초기화
    }

    //method
    public void resize(int newSize){
        Object[] b = new Object[newSize];
        for(int i=0; i<size; i++){
            b[i] = a[i];
        }
        a = (E[]) b;
    }

    public E peek(int k){ //k번째 항목을 리턴, 단순히 읽기만 한다.
        if(size == 0){
            throw new NoSuchElementException(); // underflow 경우에 프로그램 정지
        }
        return a[k-1];
    } 

    public void insertLast(E newItem){//가장 뒤에 새 항목 삽입
        if(size == a.length){
            resize(2*a.length);
        }
        a[size++] = newItem;
    }

    public void insert(int k, E newItem){//k번째 항목 뒤에 새 항목 삽입
        if(size == a.length){
            resize(2*a.length);
        }
        for(int i = size-1; i>=k-1; i--){
            a[i+1] = a[i];
        }
        a[k-1] = newItem;
        size ++;
    }

    public void delete(int k){
        for(int i=k; i<size; i++){
            a[k-1] = a[k];
        }
        size--;

        if(size == a.length/4){
            resize(a.length/2);
        }
    }

    public void print(){
        for(int i=0; i<size; i++){
           System.out.print(a[i] + "\t ");
        }
        System.out.println();
    }


    public static void main(String[] args) {
        ArrList list = new ArrList();
        list.insertLast("딸기"); list.print();
        list.insertLast("배"); list.delete(1); list.print();
    }
}
