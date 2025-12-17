package searching;

public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int start = 0;
        int end = arr.length-1;
        int target = 3;
        int mid = -1;
        while(start <= end){
            mid = (end+start)/2;
            if(arr[mid] == target){
                System.out.println("Element index: "+mid);
                break;
            }else if(arr[mid] < target){
                start = mid+1;
            }else{
                end = mid-1;
            }
        }
    }
}

/**
 * Only applicable over the sorted array.
 * Time Complexity : O(logN)
 * Also can do by recursion.
 * **/