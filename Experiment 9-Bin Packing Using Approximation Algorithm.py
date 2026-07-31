def first_fit(items, capacity=1.0):
    bins = []  # Each bin stores remaining space
    bin_contents = []
    for item in items:
        placed = False
        for i, space in enumerate(bins):
            if space >= item:
                bins[i] -= item
                bin_contents[i].append(item)
                placed = True
                break
        if not placed:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents


def first_fit_decreasing(items, capacity=1.0):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity=1.0):
    sorted_items = sorted(items, reverse=True)
    bins = []
    bin_contents = []
    for item in sorted_items:
        best_idx = -1
        best_space = float('inf')
        for i, space in enumerate(bins):
            if space >= item and space - item < best_space:
                best_space = space - item
                best_idx = i
        if best_idx >= 0:
            bins[best_idx] -= item
            bin_contents[best_idx].append(item)
        else:
            bins.append(capacity - item)
            bin_contents.append([item])
    return bin_contents


def display_bins(label, bins):
    print(f'\n{label}: {len(bins)} bins')
    for i, b in enumerate(bins, 1):
        used = sum(b)
        bar = '#' * int(used * 20)
        print(f'  Bin {i}: {[round(x, 1) for x in b]} | Used: {used:.1f} '
              f'[{bar:<20}]')


# --- NEW FEATURE: Output Efficiency Table ---
def display_efficiency_table(results, items, capacity=1.0):
    total_used = sum(items)
    
    print("\n" + "=" * 58)
    print(f"{'Algorithm':<24} | {'Bins':<5} | {'Wasted':<8} | {'Efficiency':<10}")
    print("-" * 58)
    
    for name, bins in results.items():
        num_bins = len(bins)
        total_capacity = num_bins * capacity
        wasted_space = total_capacity - total_used
        efficiency = (total_used / total_capacity) * 100 if total_capacity > 0 else 0
        
        print(f"{name:<24} | {num_bins:<5} | {wasted_space:<8.2f} | {efficiency:<9.1f}%")
        
    print("=" * 58)


# Data Setup
items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0
lower_bound = -(-sum(items) // capacity)  # Ceiling division

print(f'Items: {items}')
print(f'Capacity: {capacity}')
print(f'Sum of items: {sum(items)}')
print(f'Lower bound on bins: {int(lower_bound)}')

# Run Algorithms
ff_bins = first_fit(items)
ffd_bins = first_fit_decreasing(items)
bfd_bins = best_fit_decreasing(items)

# Display Visual Bins
display_bins('First Fit (FF)',          ff_bins)
display_bins('First Fit Decreasing (FFD)', ffd_bins)
display_bins('Best Fit Decreasing (BFD)', bfd_bins)

# Print Summary & Efficiency Table
results_dict = {
    'First Fit (FF)': ff_bins,
    'First Fit Decreasing (FFD)': ffd_bins,
    'Best Fit Decreasing (BFD)': bfd_bins
}

display_efficiency_table(results_dict, items, capacity)
