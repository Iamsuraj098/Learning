package sorting;

public class Selection {
    public static void main(String[] args) {
        int[] arr = {10, 9, 4, 11, 3, 5};
        int n = arr.length;
        for(int i=0;i<n;i++){
            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }

        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }
}