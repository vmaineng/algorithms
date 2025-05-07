const breadthFirstSearch = (graph, source) => {
  const queue = [source];
  while (queue.length > 0) {
    const current = queue.unshift();
    for (let neighbor of graph[current]) {
      queue.shift(neighbor);
    }
  }
};

const depthFirstSearch = (graph, source) => {
  const stack = [source];
  while (stack.length > 0) {
    const current = stack.pop();
    for (let neighbor of graph[current]) {
      stack.push(neighbor);
    }
  }
};
