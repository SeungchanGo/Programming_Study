package Practice;

import java.util.Stack;

public class Palindrome {
   public static boolean Palindrome_Stack(String str){
        Stack<Character> st = new Stack<Character>();
        int i;
        for(i=0; i<str.length()/2; i++){
            st.push(str.charAt(i));
        }
        if(str.length()%2 ==1){
            i++;
        }
        while(i<str.length()){
            if(st.pop()==str.charAt(i)){
                i++;
            } else {
                break;
            }
        }
        if(i == str.length()){
            return true;
        } else {
            return false;
        }
   }
    

   public static boolean Palindrome_Queue(String str){
        LinkedQueue<Character> q = new LinkedQueue<>();
        Stack<Character> st = new Stack<>();
        
        int i;
        for(i=0; i<str.length(); i++){
            q.enqueue(str.charAt(i));
            st.push(str.charAt(i));
        }
        while(!st.isEmpty()&&st.pop()==q.dequeue()){

        }
        if(st.isEmpty()){
            return true;
        } else {
            return false;
        }
        

   }

    public static void main(String[] args) {
        String str = new String("12321");
        System.out.println(Palindrome_Queue(str));
        System.out.println(Palindrome_Stack(str));
    }
}
