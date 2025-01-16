package Practice;

public class Traval {
    private Node start; //시작 섬
    public Traval(){
        start = null;
    }

    public class Node{
        //field
        private String name; // 섬 이름
        private Node left, right; // 섬 사이의 다리 연결
        
        //constructor
        private Node(String newIsland, Node lt, Node rt){ // 섬 생성자
            name = newIsland;
            left = lt;
            right = rt;
        }
    }

    public Node map(){//지도 만들기
        Node n1 = new Node("H", null, null);  Node n2 = new Node("F", null, null);
        Node n3 = new Node("S", null, null);  Node n4 = new Node("U", null, null);
        Node n5 = new Node("E", null, null);  Node n6 = new Node("Z", null, null);
        Node n7 = new Node("K", null, null);  Node n8 = new Node("N", null, null);
        Node n9 = new Node("A", null, null);  Node n10 = new Node("Y", null, null);
        Node n11 = new Node("T", null, null);  
        n1.right = n3; n1.left = n2;
        n3.right = n7; n3.left = n6;
        n7.right = n10;
        n2.right = n5; n2.left = n4;
        n5.left = n9; n9.right = n11;
        n4.left = n8;
        return n1; //시작 섬을 리턴
    }

    public void A_Course(Node n){ //A 코스
        if(n != null){
            System.out.print(n.name + "-> "); //섬 n방문
            A_Course(n.left); //왼쪽 섬 방문
            A_Course(n.right); // 오른쪽 섬 방문
        }

    }

    public void B_Course(Node n){//B 코스
        if(n != null){
            B_Course(n.left);
            System.out.print(n.name + "-> "); //섬 n방문
            B_Course(n.right);
        }       
    }
    
    public void C_Course(Node n){
        if(n != null){
            C_Course(n.left);
            C_Course(n.right);
            System.out.print(n.name + "-> "); //섬 n방문
        }       
    }

    public static void main(String[] args) {
        Traval t = new Traval();
        t.start = t.map();
        System.out.print("A코스: "); t.A_Course(t.start);
        System.out.println();
        System.out.print("B코스: "); t.B_Course(t.start);
        System.out.println();
        System.out.print("C코스: "); t.C_Course(t.start);

    }
}
