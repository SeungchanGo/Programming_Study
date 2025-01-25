package PCP2;
import java.util.concurrent.Semaphore;

// Producer-Consumenr Problem에서 busy waiting을 세마포를 통해 해결
class Buffer{
    int[] buf;
    int size, count, in, out;
    Semaphore mutex, empty, full;

    Buffer(int size){
        buf = new int[size];
        this.size = size;
        count = in = out = 0;
        mutex = new Semaphore(1);
        empty = new Semaphore(size);
        full = new Semaphore(0);
    }

    void insert(int item){
        try {
            empty.acquire();
            mutex.acquire();
        } catch (InterruptedException e){}
       
        //////////////////////////////////////
        //buf is not full
        buf[in] = item; 
        in = (in + 1) % size;
        count++;
        //////////////////////////////////////
    
        mutex.release();
        full.release();
    }

    int remove(){
        while(count == 0); 
        try {
            full.acquire();
            mutex.acquire();
        } catch (InterruptedException e){}
        
        //////////////////////////////////////
        //buf is not empty
        int item = buf[out]; 
        out = (out+1) % size;
        count--;
        //////////////////////////////////////
        
        mutex.release();
        empty.release();
        return item;
    }
}

class Producer extends Thread {
    Buffer b;
    int n;
    Producer(Buffer b, int n){
        this.b = b;
        this.n = n;
    }
    
    public void run(){
        for(int i=0; i<n; i++){
            b.insert(i);
        }
    }
}

class Consumer extends Thread{
    Buffer b;
    int n;
    Consumer(Buffer b, int n){
        this.b = b;
        this.n = n;
    }

    public void run(){
        int item;
        for(int i=0; i<n; i++){
            item = b.remove();
        }
    }
}

class Test6 {
    public static void main(String[] args) {
        Buffer b = new Buffer(100);
        Producer p = new Producer(b, 10000);
        Consumer c = new Consumer(b, 10000);
        p.start();
        c.start();
        try {
            p.join();
            c.join();
        } catch (InterruptedException e){}
        System.out.println("Number of items in the buf is " + b.count);
    }
}