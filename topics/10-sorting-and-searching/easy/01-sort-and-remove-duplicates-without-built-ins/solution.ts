function siftDown(arr: number[], heapSize: number, root: number): void {
  while (true) {
    let largest = root;
    const left = 2 * root + 1;
    const right = left + 1;

    if (left < heapSize && arr[left] > arr[largest]) {
      largest = left;
    }
    if (right < heapSize && arr[right] > arr[largest]) {
      largest = right;
    }
    if (largest === root) {
      return;
    }

    const temporary = arr[root];
    arr[root] = arr[largest];
    arr[largest] = temporary;
    root = largest;
  }
}

function heapSort(arr: number[]): void {
  for (let root = Math.floor(arr.length / 2) - 1; root >= 0; root -= 1) {
    siftDown(arr, arr.length, root);
  }

  for (let end = arr.length - 1; end > 0; end -= 1) {
    const temporary = arr[0];
    arr[0] = arr[end];
    arr[end] = temporary;
    siftDown(arr, end, 0);
  }
}

function sortAndRemoveDuplicates(arr: number[]): number {
  if (arr.length === 0) {
    return 0;
  }

  heapSort(arr);
  let write = 1;

  for (let read = 1; read < arr.length; read += 1) {
    if (arr[read] !== arr[write - 1]) {
      arr[write] = arr[read];
      write += 1;
    }
  }

  return write;
}

function distinctValues(arr: number[], count: number): number[] {
  const result: number[] = [];
  for (let index = 0; index < count; index += 1) {
    result[result.length] = arr[index];
  }
  return result;
}

const tests: number[][] = [
  [4, 2, 4, 1, 3, 2],
  [5, 5, 5, 5],
  [-1, 3, -1, 2, 3, 0],
  [],
  [7],
];

for (let index = 0; index < tests.length; index += 1) {
  const count = sortAndRemoveDuplicates(tests[index]);
  console.log(distinctValues(tests[index], count));
}
