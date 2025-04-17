from functools import wraps
import time
import tracemalloc

def strategy_benchmark(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = func(*args, **kwargs)
    
    # Handle different return formats
    if isinstance(result, tuple) and len(result) == 2:
        move, n_expanded_nodes = result
    else:
        move = result
        n_expanded_nodes = 1  # Default value if not provided

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # For pygame implementation, we'll return metrics rather than printing
    execution_time = end_time - start_time
    memory_used = peak / 10**3  # KB
    
    # Print stats in console mode for debugging
    print(f"\nBenchmark for `{func.__name__}`:")
    print(f"⏱️ Execution time: {execution_time:.6f} seconds")
    print(f"📦 Memory used during execution: {memory_used:.3f} KB")
    print(f"🔍 Number of expanded nodes: {n_expanded_nodes}\n")
    
    return move, n_expanded_nodes
  return wrapper


