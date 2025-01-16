package Practice;

public class Sort {
    //기본 메소드
    public static void swap(int[] a, int i, int j){
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    public static void print(int[] a){
        for(int item:a){
            System.out.print(item + " ");
        }
        System.out.println();
    }

    public static void selectSort(int a[]){
        for(int i=0; i<a.length-1; i++){
            int min = i;
            for(int j=i+1; j<a.length; j++){
                if(a[min] > a[j]){
                    min = j;
                }
            }
            swap(a, i, min);
            print(a);
        }
    }

    public static void bubbleSort(int a[]){
        for(int i=a.length-1; i>0; i--){
            for(int j=0; j<i; j++){
                if(a[j+1] < a[j]){
                    swap(a, j, j+1);
                }
            }
            print(a);
        }
    }

    public static void insertSort(int a[]){
        for(int i=1; i<a.length; i++){
            int j = i-1;
            int newItem = a[i];
            while(j>=0 && a[j] > newItem){
                a[j+1] = a[j];
                j--;
            }
            a[j+1] = newItem;
            print(a);
        }
    }



    public static void main(String[] args) {
        int[] a = {180, 175, 186, 172, 163, 169, 188};
        selectSort(a);
        System.out.println();
        int[] b = {180, 175, 186, 172, 163, 169, 188};
        bubbleSort(b);
        System.out.println();
        int[] c = {180, 175, 186, 172, 163, 169, 188};
        insertSort(c);
        System.out.println();
    }




}
