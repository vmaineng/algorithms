// Challenge: try to figure out how to move the nested address object type
// into a separate type definition. When done correctly, there should be no more
// red errors in the editor

type Address = {
     street: string
        city: string
        country: string
    
}

type Person = {
    name: string
    age: number
    isStudent: boolean
    address: Address
}

let person1: Person = {
    name: "Joe",
    age: 42,
    isStudent: true,
    address: {
        street: "123 Main",
        city: "Anytown",
        country: "USA"
    }
}

let person2: Person = {
    name: "Jill",
    age: 66,
    isStudent: false,
    address: {
        street: "123 Main",
        city: "Anytown",
        country: "USA"
    }
}

let people = [person1, person2]

type Order = 'ordered' | 'completed'

type identifier = string | number

function getPizzaDetail(identifier:identifier) {
    if (identifier === 'string') {
        menubar.find(getPizzaDetail.name.toLowerCase())
    } else if (identifier === 'number') { 
        menubar.find(pizza => pizza.id === identifier)
    }
}

type User = {
    id: number
    username: string
    role: "member" | "contributor" | "admin"
}

const users: User[] = [
    { id: 1, username: "john_doe", role: "member" },
    { id: 2, username: "jane_smith", role: "contributor" },
    { id: 3, username: "alice_jones", role: "admin" },
    { id: 4, username: "charlie_brown", role: "member" },
];

function updateUser(id: number, updates: any) {
    // Find the user in the array by the id
    // Use Object.assign to update the found user in place. 
    // Check MDN if you need help with using Object.assign

    const foundUser = users.find(user=> user.id === id)

    if (!foundUser) { 
        console.error("user not found")
        return
    }
    Object.assign(foundUser, updates)
}

// Example updates:
updateUser(1, { username: "new_john_doe" });
updateUser(4, { role: "contributor" });

console.log(users)

type User = {
    id: number
    username: string
    role: "member" | "contributor" | "admin"
}

type UpdatedUser = Partial<User>

let nextUserId = 1

const users: User[] = [
    { id: nextUserId++, username: "john_doe", role: "member" },
    { id: nextUserId++, username: "jane_smith", role: "contributor" }
];

function updateUser(id: number, updates: UpdatedUser) {
    const foundUser = users.find(user => user.id === id)
    if (!foundUser) {
        console.error("User not found!")
        return
    }
    Object.assign(foundUser, updates)
}

// updateUser(1, { username: "new_john_doe" });
// updateUser(4, { role: "contributor" });

function addNewUser(newUser: any): User {
    // Create a new variable called `user`, add an `id` property to it
    // and spread in all the properties of the `newUser` object. Think
    // about how you should set the type for this `user` object.
    // Push the new object to the `users` array, and return the object
    // from the function at the end


    const user: User = { id: nextUserId++, ...newUser } 
    users.push(user)
    return user
}

// example usage:
addNewUser({ username: "joe_schmoe", role: "member" })

console.log(users)

select BroadcastChannel, model, color price from cars WHERE color = 'black'

SELECT brand, model, condition, price FROM cars 
WHERE condition = 0

SELECT brand, model, condition, price FROM cars
WHERE condition > 3

SELECT brand, model, condition, price FROM cars
WHERE price < 50000


SELECT brand, model,color, price FROM cars
WHERE color != 'yellow'