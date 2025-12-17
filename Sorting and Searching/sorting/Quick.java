package sorting;

public class Quick {

    static int partition(int[] arr, int start, int end){
        int pivot = arr[end];
        int i = start-1;

        for(int j=start;j<=end-1;j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i+1, end);
        return i+1;
    }

    static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static void sort(int[] arr,int start, int end){
        if(start < end){
            int pivot = partition(arr, start, end);

            sort(arr, start, pivot-1);
            sort(arr, pivot+1, end);
        }
    }
    public static void main(String[] args) {
        int[] arr = {10, 9, 4, -1, 3};
        int n = arr.length;
        sort(arr, 0,n-1);
        for (int j : arr) {
            System.out.print(j + " ");
        }
    }
}
