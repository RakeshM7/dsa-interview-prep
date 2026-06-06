public class Solution {
    private static void siftDown(int[] arr, int heapSize, int root) {
        while (true) {
            int largest = root;
            int left = 2 * root + 1;
            int right = left + 1;

            if (left < heapSize && arr[left] > arr[largest]) {
                largest = left;
            }
            if (right < heapSize && arr[right] > arr[largest]) {
                largest = right;
            }
            if (largest == root) {
                return;
            }

            int temporary = arr[root];
            arr[root] = arr[largest];
            arr[largest] = temporary;
            root = largest;
        }
    }

    private static void heapSort(int[] arr) {
        for (int root = arr.length / 2 - 1; root >= 0; root--) {
            siftDown(arr, arr.length, root);
        }

        for (int end = arr.length - 1; end > 0; end--) {
            int temporary = arr[0];
            arr[0] = arr[end];
            arr[end] = temporary;
            siftDown(arr, end, 0);
        }
    }

    public static int sortAndRemoveDuplicates(int[] arr) {
        if (arr.length == 0) {
            return 0;
        }

        heapSort(arr);
        int write = 1;

        for (int read = 1; read < arr.length; read++) {
            if (arr[read] != arr[write - 1]) {
                arr[write] = arr[read];
                write++;
            }
        }

        return write;
    }

    private static void printDistinctValues(int[] arr, int count) {
        System.out.print("[");
        for (int index = 0; index < count; index++) {
            if (index > 0) {
                System.out.print(", ");
            }
            System.out.print(arr[index]);
        }
        System.out.println("]");
    }

    public static void main(String[] args) {
        int[][] tests = {
            {4, 2, 4, 1, 3, 2},
            {5, 5, 5, 5},
            {-1, 3, -1, 2, 3, 0},
            {},
            {7}
        };

        for (int[] values : tests) {
            int count = sortAndRemoveDuplicates(values);
            printDistinctValues(values, count);
        }
    }
}
