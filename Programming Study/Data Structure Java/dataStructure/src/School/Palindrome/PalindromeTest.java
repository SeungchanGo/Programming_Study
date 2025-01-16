package Palindrome;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class PalindromeTest {
    public static boolean palindromeTest_Stack(String str){
        Stack<Character> st = new Stack<Character>();
        int i = 0;
        for(i=0; i<str.length()/2; i++){
            st.push(str.charAt(i));
        }

        if(str.length()%2 == 1){
            i++;
        }

        while(i<str.length()){
            if(st.pop() == str.charAt(i)){
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


    public static boolean palindromeTest_Queue(String str){
        Stack<Character> st = new Stack<Character>();
        Queue<Character> q = new LinkedList<Character>();

        int i=0;
        for(i=0; i<str.length(); i++){
            st.push(str.charAt(i));
            q.add(str.charAt(i));
        }

        while(!st.isEmpty() && st.pop() == q.remove()){
        }
        if(st.isEmpty()){
            return true;
        } else {
            return false;
        }
    } 
}
