# K17Coins

## Intended Solution

Race Condition. See solve.py

## Unintended Solution

Amount was not checked when transferring.

Just transfer a negative amount.

That's why you shouldn’t write a challenge at 3 o’clock in the morning.

To fix it, patch `FIX_UNINTENDED_BUG.patch`

To ensure fairness, this patch was not applied during the competition.
