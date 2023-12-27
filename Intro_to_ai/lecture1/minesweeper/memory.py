import tracemalloc

tracemalloc.start(10)


with open("runner.py") as f:
    exec(f.read())

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
