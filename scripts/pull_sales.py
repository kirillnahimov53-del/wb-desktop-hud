import csv, os
os.makedirs("data", exist_ok=True)
with open("data/sales.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["orders_today"])
    w.writerow([5])
print("ok")
