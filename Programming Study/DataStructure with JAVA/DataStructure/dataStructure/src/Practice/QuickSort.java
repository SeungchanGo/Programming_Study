package Practice;

public class QuickSort {
     // 퀵 정렬
     public static void quickSort(int [] a, int p, int r){
        // p: 정렬할 배열의 시작 위치, r: 정렬할 배열의 마지막 위치 = 피벗
        if(p<r){
            //기준원소를 기준으로 작은 원소, 큰 원소를 각각 나누어 분할
            int pivot = partition(a, p, r);
            //왼쪽 부분배열(피벗보다 작은 값들로 구성된)을 정렬
            quickSort(a, p, pivot-1);
            //오른쪽 부분배열(피벗보다 큰 값들로 구성된)을 정렬
            quickSort(a, pivot+1, r);
        }
    }

    // 분할 알고리즘
    public static int partition(int[] a, int p, int r){
        int x = a[r]; // 기준 원소는 배열의 마지막 원소
        int i = p-1;
        for(int j=p; j<=r-1; j++){
            if(a[j] < x){
                swap(a, ++i, j); 
            }
        }
        // a[r] <-> a[i+1]
        swap(a, r, i+1);
        //partition(a, p, r) 호출 후 배열의 상태를 출력
        System.out.printf("a[%d] : %d => ", r, x);
        print(a);

        // 피벗의 위치 반환
        return i+1;
    }
    public static void main(String[] args) {
        
    }

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
}
