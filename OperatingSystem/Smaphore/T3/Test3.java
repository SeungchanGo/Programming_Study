package T3;
import java.util.concurrent.Semaphore;

// 세마포를 두개 사용하여 실행할 때 무조건 Parent부터 실행되도록 함
class BankAccount{
        int balance;
        Semaphore sem, sem1;
        
        BankAccount() {
            sem = new Semaphore(1);
            sem1 = new Semaphore(0);  
        }
        
        void deposit(int amount){
            try{
                sem.acquire();   
            }catch (InterruptedException e){ }
                ////////////////////////////////////////////////
                int temp = balance + amount;  //balance = balance + amount;
                System.out.print("+");
                balance = temp;
                ///////////////////////////////////////////////
                sem.release();
                sem1.release(); 
            }
           
        void withdraw(int amount){
            try{
                sem1.acquire();
                sem.acquire();   
            }catch (InterruptedException e){ }
                ////////////////////////////////////////////////
                int temp = balance - amount;  //balance = balance - amount;
                System.out.print("-");
                balance = temp;
                ///////////////////////////////////////////////
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


public class Test3 {
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
