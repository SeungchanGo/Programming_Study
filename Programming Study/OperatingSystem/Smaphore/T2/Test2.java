package T2;
import java.util.concurrent.Semaphore;

// 세마포를 사용하여 critical section problem 해결(mutual exclusion)
class BankAccount{
    int balance;
    Semaphore sem;
    BankAccount(){
        sem = new Semaphore(1);
    }

    void deposit(int n){
        try{
            sem.acquire();
        } catch(InterruptedException e){}
        /////////////////////////
        int temp = balance + n;
        System.out.print("+");
        balance = temp;
        /////////////////////////
        sem.release();
    }

    void withdraw(int n){
        try{
            sem.acquire();
        } catch(InterruptedException e){}
        /////////////////////////
        int temp = balance - n;
        System.out.print("-");
        balance = temp;
        /////////////////////////
        sem.release();
    }

    int getBalance(){
        return balance;
    }
}

// 부모 쓰레드
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


class test2{
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
