function taskAssignment(k, tasks) {
  //receive number of workers (k) and an array of positive integers
  //return min total time and pair tasks

  //sort the tasks from smallest to biggest
  //pair the smallest with the biggest duration
  //continue pairing until all tasks are assigned

  const taskIndices = tasks.map((task, index) => [task, index]);
  //taskIndices = [[1, 0], [3, 1], [5, 2], [3, 3], [1, 4], [4, 5]]

  taskIndices.sort((a, b) => a[0] - b[0]);
  //sort by task
  //ex: [[1, 0], [1, 4], [3, 1], [3, 3], [4, 5], [5, 2]]

  const pairs = [];

  let left = 0;
  let right = taskIndices.length - 1;

  while (left < right) {
    const pair = [taskIndices[left][1], taskIndices[right][1]];
    //taskIndices[left][1] = b/c need index
    //taskIndices[left][0] would access the taskDuration.
    //taskIndices[left][1] accesses the originalIndex.

    pairs.push(pair);
    left++;
    right--;
  }
  return pairs;
}

// Do not edit the line below.
exports.taskAssignment = taskAssignment;
