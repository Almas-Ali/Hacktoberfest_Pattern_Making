import java.util.Arrays;

public class SortingIDs {
    public static void main(String[] args) {
        int[] arr = {34, 02, 13, 25, 43, 12, 04, 21};
        insertionSortIntermediate(arr);
        System.out.println("Array sorted in ascending order of the second digit = "+ Arrays.toString(arr));
        insertionSort(arr);
        System.out.println("Sorted array in ascending order = "+ Arrays.toString(arr));
    }
    static int[] insertionSortIntermediate(int[] arr){
        int[] Array;
        for(int i=1; i< arr.length;i++){
            int key = arr[i];
            int j = i-1;

            while (j>=0 && (key%10)<(arr[j]%10)){
                arr[j+1] = arr[j];
                --j;
            }
            arr[j+1]=key;
        }
        Array = arr;
        return Array;
    }

    static void insertionSort(int[] arr){
        int[] Array = insertionSortIntermediate(arr);
        for(int i=1; i< Array.length;i++){
            int key = Array[i];
            int j = i-1;

            while (j>=0 && key<Array[j]){
                Array[j+1] = Array[j];
                --j;
            }
            Array[j+1]=key;
        }

    }

}