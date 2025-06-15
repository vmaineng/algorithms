const UserProfile = () => {
  const [user, setUser] = useState<{ name: string; email: string } | null>(
    null
  );

  useEffect(() => {
    fetchUser().then(setUser);
  }, []);

  return (
    <div className="profile">
      {user ? (
        <>
          <div className="profile-header">
            <h1>{user.name}</h1>
            <p>{user.email}</p>
          </div>
          <button onClick={() => alert("Edit profile")}>Edit</button>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

//put out loading out to its own
//use try-catch with useEffect
//create a separate userInfo component

import { useState, useEffect } from "react";

const TaskManager = () => {
  const [tasks, setTasks] = useState<any[]>([]);
  const [newTask, setNewTask] = useState("");
  const [loading, setLoading] = useState(false);
  const [filter, setFilter] = useState<"all" | "active" | "completed">("all");

  useEffect(() => {
    setLoading(true);
    fetch("https://jsonplaceholder.typicode.com/todos")
      .then((res) => res.json())
      .then((data) => setTasks(data.slice(0, 5)))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  const addTask = () => {
    if (newTask.trim()) {
      setTasks([
        ...tasks,
        { id: Date.now(), title: newTask, completed: false },
      ]);
      setNewTask("");
    }
  };

  const toggleTask = (id: number) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  const filteredTasks = tasks.filter((task) => {
    if (filter === "active") return !task.completed;
    if (filter === "completed") return task.completed;
    return true;
  });

  return (
    <div className="task-manager">
      <h1>Task Manager</h1>
      <div className="task-form">
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Add a new task"
        />
        <button onClick={addTask}>Add Task</button>
      </div>
      <div className="task-filters">
        <button onClick={() => setFilter("all")}>All</button>
        <button onClick={() => setFilter("active")}>Active</button>
        <button onClick={() => setFilter("completed")}>Completed</button>
      </div>
      {loading ? (
        <p>Loading tasks...</p>
      ) : (
        <ul className="task-list">
          {filteredTasks.map((task) => (
            <li key={task.id}>
              <input
                type="checkbox"
                checked={task.completed}
                onChange={() => toggleTask(task.id)}
              />
              <span
                style={{
                  textDecoration: task.completed ? "line-through" : "none",
                }}
              >
                {task.title}
              </span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default TaskManager;

//Name Component
interface NameProps {
  name: string;
}

function NameChange({ name }: NameProps) {
  return <div>"Hello {name}"</div>;
}

import { name } from "./NameChange";

function greetUser() {
  return <div>if (name) return 'Hello {name}' else "Hello!"</div>;
}

interface GreetUserProps {
  name?: string;
}

export function GreetUser({ name }: GreetUserProps) {
  const knownNames = new Set(["Alice", "Bob", "Charlie"]);
  const greeting = name && knownNames.has(name) ? "Hello ${name}!" : "Hello!";

  return <div> {greeting}</div>;
}
