### Orderbook Prioritization 

A Swap Execution Facility (SEF) is a platform for swapping derivatives that provides pre-trade transparency and promotes fair trading. The Commodity Futures Trading Commission (CFTC) established the SEF framework as part of the Dodd-Frank Wall Street Reform and Consumer Protection Act in response to the 2008 financial crisis.

In a SEF, participants can submit bids (buy orders) and offers (sell orders) for a specific financial instrument, which are then prioritized in an order book. This book keeps track of all bids and offers for a specific instrument and plays a crucial role in ensuring the market's fairness and transparency.

The SEF generally prioritizes bids and offers in the order book based on the Price-Time Priority principle. Here's how it works:

1. **Price Priority**: Orders with better prices are given priority over orders with worse prices. For example, the highest price bid (buy order) and the lowest price offer (sell order) are considered the best prices. When a bid and an offer match in terms of price, a transaction can occur.

2. **Time Priority**: If two or more orders have the same price, the order that was placed first has priority. This means that if two participants submit a bid for the same price, the one who submitted it first will have their order filled first.

Now, regarding the types of orders we discussed earlier, namely Fill or Kill (FOK) and All or None (AON) orders, how they are prioritized in an order book can vary based on the rules of the specific SEF. However, in general:

- **FOK Orders**: Given the immediate nature of these orders, they would be prioritized in the price-time priority queue if the full volume is available at the best price. If the full volume isn't available, the order would be immediately canceled.

- **AON Orders**: An AON order can sit in the order book and wait until it can be fully executed, even if that means the order isn't filled right away. If a partial match becomes available, it will be ignored in favor of orders that can be fully filled or partially filled without such restrictions.

1.	Fill or Kill (FOK) Orders: These orders mandate that unless an order can be filled entirely, it should be canceled (killed) immediately. In essence, a FOK order ensures that the trader gets the entire quantity of the security they want or none at all. Importantly, FOK orders do not allow any partial filling; the order must be filled in its entirety as soon as it's issued, or it will be canceled. FOK orders demand immediacy, requiring the complete fulfillment of the order as soon as it is placed or its immediate cancellation if full fulfillment isn't possible. Given their immediate nature, they would be prioritized in a price-time priority queue if the full volume is available at the best price. If the full volume isn't available at the best price, the order would be immediately canceled.
2.	All or None (AON) Orders: Similar to FOK orders, AON orders specify that the order should be filled in its entirety or not at all. However, unlike FOK orders, there's no immediate urgency attached to AON orders. They can remain open or active until they are either filled entirely or the trader chooses to cancel them. This means an AON order could sit on the order book for an extended period, waiting for the right conditions to be met for it to be filled completely. AON orders differ in that they require the full quantity to be executed, but they don't demand immediate execution. An AON order will remain in the order book until the full quantity can be matched, even if that means the order isn't filled right away. As a result, an AON order does not disrupt the price-time priority; it can sit in the order book and wait until it can be fully executed. If a partial match becomes available, it will be ignored in favor of orders that can be fully filled or partially filled without such restrictions.

The AON orders, while respecting the price part of price-time priority, do not strictly respect the time component. When it comes to executing transactions, a newer non-AON order could get executed before an older AON order if the AON order cannot yet be filled in its entirety, even though the AON order arrived first. However, an AON order will always have priority over later AON or non-AON orders at the same price once its execution conditions are met.
