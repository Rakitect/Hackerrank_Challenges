def print_transactions(m, k, d, names, owned, prices):
    # Simple trend-based strategy
    for i in range(k):
        name = names[i]
        owned_shares = owned[i]
        price_series = prices[i]

        recent = price_series[-3:]  # last 3 days
        trend_up = all(x < y for x, y in zip(recent, recent[1:]))
        trend_down = all(x > y for x, y in zip(recent, recent[1:]))

        current_price = price_series[-1]

        if trend_up:
            quantity = int(m // current_price)
            if quantity > 0:
                print(f"BUY {name} {quantity}")
                return
        elif trend_down and owned_shares > 0:
            print(f"SELL {name} {owned_shares}")
            return

    print("HOLD")


# Read input like main()
if __name__ == "__main__":
  targets = input().strip().split();
  if len(targets) != 3:
    sys.exit("Invalid input: expected 3 targets.")
  
  m = float(input())
  k = int(input())
  d = int(input())

  names = []
  owned = []
  prices = []

  for _ in range(k):
    parts = input().strip().split()
    names.append(parts[0])
    owned.append(int(parts[1]))
    price_list = list(map(float, parts[2:]))
    prices.append(price_list)

  print_transactions(m, k, d, names, owned, prices)
