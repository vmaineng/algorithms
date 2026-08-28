import React from "react";

export default function App() {
  const [unreadMessages, setUnreadMessages] = React.useState(["a", "b"]);

  /**
   * Challenge:
   * Only display the <h1> below if there are unread messages
   */

  return (
    <div>
      {unreadMessages.length > 0 && (
        <h1>You have {unreadMessages.length} unread messages!</h1>
      ): (
        <p>You have no unread messages.</p>
      )}
    </div>
  );
}

import React from "react"

export default function Joke(props) {
    const [isShown, setIsShown] = React.useState(false)
    
    function toggleShown() {
        setIsShown(prevShown => !prevShown)
    }
    
    return (
        <div>
            {props.setup && <h3>{props.setup}</h3>}

    {isShown ? (
        <>
            <p>{props.punchline}</p>
            <button onClick={toggleShown}>Close Punchline</button>
        </>
    ) : (
        <button onClick={toggleShown}>Show punchline</button>
    )}

            <hr />
        </div>
    )
}

const menu = [
    { name: "Margherita", price: 8 },
    { name: "Pepperoni", price: 10 },
    { name: "Hawaiian", price: 10 },
    { name: "Veggie", price: 9 },
]

const cashInRegister = 100
const orderQueue = []

/**
 * Challenge: Add a utility function "addNewPizza" that takes a pizza object
 * and adds it to the menu.
 */


function addNewPizza(pizzaObj) { 
    menu.push(pizzaObj)

}

function placeOrder(pizzaName) {
    const pizzaName = menu.find(pizzaObj => pizzaName === pizzaObj)
    cashInRegister += pizzaName.price
    orderQueue.push(pizzaName.name)
}



function completeOrder(orderId) { 
    const order = orderQueue.find(order => order.id === orderId)
    order.status = 'completed'
    return order
}
