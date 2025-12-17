package sorting;

public class Merge {

    public static void merge(int[] arr, int start, int mid, int end) {
        int left = mid - start+1;
        int right = end - mid;
        int i;
        int j;
        int k = start;
        int[] lef_arr = new int[left];
        int[] rig_arr = new int[right];

        for (i=0;i<left;i++) {
            lef_arr[i] = arr[start + i];
        }

        for (j=0;j<right;j++) {
            rig_arr[j] = arr[mid + 1 + j];
        }
        i = 0;
        j = 0;

        while (i < left && j < right) {
            if (lef_arr[i] <= rig_arr[j]) {
                arr[k] = lef_arr[i];
                i++;
            } else {
                arr[k] = rig_arr[j];
                j++;
            }
            k++;
        }

        while(i < left){
            arr[k] = lef_arr[i];
            i++;
            k++;
        }

        while(j < right){
            arr[k] = rig_arr[j];
            j++;
            k++;
        }
    }

    public static void sort(int[] arr, int start, int end){
        if(start < end){
            int mid = (end+start)/2;
            sort(arr, start, mid);
            sort(arr, mid+1, end);
            merge(arr, start, mid, end);
        }
        return;
    }

    public static void main(String[] args) {
        int[] arr = {10, 9, 4, 11, 3};
        int n = arr.length;
        sort(arr, 0, n-1);
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+" ");
        }
    }
}