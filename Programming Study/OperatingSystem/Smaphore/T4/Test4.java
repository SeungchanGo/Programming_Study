package T4;
import java.util.concurrent.Semaphore;

// 세마포를 사용하여 Parent와 Child의 Thread를 번갈아가면서 하게함.
class BankAccount {
    int balance;
    Semaphore sem;
    Semaphore dsem, wsem;
    BankAccount(){
        sem = new Semaphore(1);
        dsem = new Semaphore(0);
        wsem = new Semaphore(0);
    }

    void deposit(int amount){
        try{
            sem.acquire();
        } catch (InterruptedException e){}

        //////////////////////////////////////
        int temp = balance + amount;
        System.out.print("+");
        balance = temp;
        //////////////////////////////////////
        
        sem.release();
        wsem.release();
        try{
            dsem.acquire();
        } catch(InterruptedException e){}
    }

    void withdraw(int amount){
        try{
            wsem.acquire();
            sem.acquire();
        } catch(InterruptedException e){}
        //////////////////////////////////////
        int temp = balance - amount;
        System.out.print("-");
        balance = temp;
        //////////////////////////////////////
        sem.release();
        dsem.release();
    }

    int getBalance(){
        return balance;
    }
}

class Parent extends Thread{
    BankAccount b;
    Parent(BankAccount b){
        this.b = b;
    }

    public void run(){
        for(int i=0; i<1000; i++){
            b.deposit(1000);
        }
    }
}

// 자식 쓰레드
class Child extends Thread{
    BankAccount b;
    Child(BankAccount b){
        this.b = b;
    }

    public void run(){
        for(int i=0; i<1000; i++){
            b.withdraw(1000);
        }
    }
}


public class Test4 {
    public static void main(String[] args) throws InterruptedException {
        BankAccount b = new BankAccount();
        Parent p = new Parent(b);
        Child c = new Child(b);
        p.start();
        c.start();
        p.join();
        c.join();
        System.out.print("Balance = " + b.getBalance());
    }
}