import Deque.ArrayDeque;
public class Main {
    public static void main(String[] args) {
        ArrayDeque<Integer> arr = new ArrayDeque<Integer>();
        arr.insertFront(1);
        arr.insertFront(2);
        arr.insertFront(3);
        arr.insertLast(0);
        System.out.println(arr);

        int a = arr.deleteFront();
        System.out.println("삭제된 원소:" + a);
        System.out.println(arr);

    }
    
}
