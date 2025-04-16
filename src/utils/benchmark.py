from functools import wraps
import time
import tracemalloc

def strategy_benchmark(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()
    start_snapshot = tracemalloc.take_snapshot()

    move, n_expanded_nodes = func(*args, **kwargs)

    end_snapshot = tracemalloc.take_snapshot()
    end_time = time.perf_counter()
    tracemalloc.stop()

    stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    total_memory_used = sum(stat.size_diff for stat in stats)

    print(f"\nBenchmark for `{func.__name__}`:")
    print(f"⏱️ Execution time: {end_time - start_time:.6f} seconds")
    print(f"📦 Memory used during execution: {total_memory_used / 10**3:.3f} KB")
    print(f"?? Number of expanded nodes: {n_expanded_nodes}\n")
    
    return move
  return wrapper

    
        