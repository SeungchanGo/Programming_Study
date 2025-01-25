package T5;
import java.util.concurrent.Semaphore;

// P1->P2->P3 순으로 실행하도록 세마포를 사용
class BankAccount {
    int balance;
    Semaphore dsem, wsem1, wsem2;
    BankAccount(){
        dsem = new Semaphore(0);
        wsem1 = new Semaphore(0);
        wsem2 = new Semaphore(0);
    }

    void deposit(int amount){
        
        //////////////////////////////////
        int temp = balance + amount;
        System.out.print("D ");
        balance = temp;
        //////////////////////////////////////
        
        wsem1.release();
        try{
            dsem.acquire();
        } catch(InterruptedException e){}////
    }

    void withdraw1(int amount){
        try{
            wsem1.acquire();
        } catch(InterruptedException e){}
        
        //////////////////////////////////////
        int temp = balance - amount;
        System.out.print("W1 ");
        balance = temp;
        //////////////////////////////////////
        
        wsem2.release();
    }

    void withdraw2(int amount){
        try{
            wsem2.acquire();
        } catch(InterruptedException e){}
        
        //////////////////////////////////////
        int temp = balance - amount;
        System.out.print("W2 ");
        balance = temp;
        //////////////////////////////////////
        
        dsem.release();
    }

    int getBalance(){
        return balance;
    }
}

class P1 extends Thread{
    BankAccount b;
    P1(BankAccount b){
        this.b = b;
    }

    public void run(){
        for(int i=0; i<100; i++){
            b.deposit(2000);
        }
    }
}

class P2 extends Thread{
    BankAccount b;
    P2(BankAccount b){
        this.b = b;
    }

    public void run(){
        for(int i=0; i<100; i++){
            b.withdraw1(1000);
        }
    }
}

class P3 extends Thread{
    BankAccount b;
    P3(BankAccount b){
        this.b = b;
    }

    public void run(){
        for(int i=0; i<100; i++){
            b.withdraw2(1000);
        }
    }
}


public class Test10 {
    public static void main(String[] args) throws InterruptedException {
        BankAccount b = new BankAccount();
        P1 p1 = new P1(b);
        P2 p2 = new P2(b);
        P3 p3 = new P3(b);
        p1.start();
        p2.start();
        p3.start();
        p1.join();
        p2.join();
        p3.join();
        System.out.print("Final balance = " + b.getBalance());
    }
}