// You are given an array prices where prices[i] is the price of a
//  given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and 
// choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this
//  transaction. If you cannot achieve any profit, return 0.

 

// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 
// (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you 
// must buy before you sell.

const stock = (array) => {
    //an array of integers (positive and negative)
    //return max profit (buy -  sell)
    //stock([1,2]) => buy the stock for 1, and sell for 2; //return 0; b/c wouldve been -1;
    //buy high, sell low

    //brute force; 
    //we can look at each possible pair and calculate the profit,
    //then you can find the pair of dates that has the highest total
    //initialize profit
    
    let maxProfit = 0;
    
    // for (let i = 0; i < array.length; i++) { //i= buy
    //     for (j = i + 1; j < array.length; j++) { //sell
    //         profit = array[j] - array[i]
    //         if (profit > maxProfit)  {
    //             console.log
    //           maxProfit = profit;

    //         }
    //     }   
    // }

    // return maxProfit;

    //optimized method:
    let sell = 0; 
    let buy = sell + 1;

    while (buy < array.length) {
        if (array[sell] < array[buy]) {
        profit = array[buy] - array[sell]

        maxProfit = Math.max(profit, maxProfit)

    } else {
        sell = buy
        console.log(buy, sell)
        // console.log(array[buy], array[sell])
    }
    buy++;
    }

    return maxProfit
}

console.log(stock([4,6,7,6,5,1,7])) 
//buy 1, sell 3 = 2