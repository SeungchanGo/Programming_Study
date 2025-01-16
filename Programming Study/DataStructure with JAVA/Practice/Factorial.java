package Practice;

public class Factorial{
    public static int factorial1(int n){
        if(n <= 1){
            return 1;
        } else{
            return n*factorial1(n-1);
        }
    }

    public static void factorial2(int n){
        int result = 1;
        for(int i=1; i<=n; i++){
            result = i*result;
        }
        System.out.println(result);
    }

    public static void main(String[] args){
        int result;
        result = factorial1(4);
        System.out.println(result);

        factorial2(4);

    }
}