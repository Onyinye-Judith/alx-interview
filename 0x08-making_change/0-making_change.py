#!/usr/bin/python3

def makeChange(coins, total):
        min_coins = [total + 1] * (total + 1)
            min_coins[0] = 0

                for amount in range(1, total + 1):
                            for coin in coins:
                                            if coin <= amount:
                                                                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

                                                                    return -1 if min_coins[total] > total else min_coins[total]
