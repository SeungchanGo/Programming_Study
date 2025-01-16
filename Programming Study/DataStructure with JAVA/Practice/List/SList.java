package Practice.List;

public class SList <E> {
    //field
    protected Node head;
    private int size;
    
    //constructor
    public SList(){
        head = null;
        size = 0;
    }
    
    //method
    public int search(E target){
        Node p = head;
        for(int k=0; k<size; k++){
            if(target==p.getItem()){
                return k;
            }
            p = p.getNext();
        }
        return -1;
    }

    public Node peek(int k){
        Node p = head;
        if(k==1){ 
            return p;
        }
        for(int i=0; i<k-2; i++){
            p = p.getNext();
        }
        return p;
    }

    public void insertFront(E newItem){
        head = new Node(newItem, head);
        size++;
    }

    public void insertAfter(E newItem, Node p){
        p.setNext(new Node(newItem, p.getNext()));
        size++;
    }

    public void deleteAfter(Node p){
        Node t = p.getNext();
        p.setNext(t.getNext());
        t.setNext(null);
        size--;
    }

    public void deleteFront(){
        head = head.getNext();
        size--;
    }

    public void print(){
        Node p = head;
        for(int i=0; i<size; i++){
            System.out.print(p.getItem() + "\t");
            p = p.getNext();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        SList sl = new SList();
        sl.insertFront("딸기"); sl.insertAfter("배", sl.peek(1));
        sl.insertFront("오렌지"); sl.insertAfter("귤", sl.peek(2));
        sl.print();
        sl.insertAfter("땅콩", sl.peek(4)); sl.insertAfter("사과", sl.peek(3));
        sl.insertFront("감"); sl.insertFront("포도");
        sl.print();
        sl.deleteAfter(sl.peek(8)); sl.deleteAfter(sl.peek(7));
        sl.print();


    }

 }

    

