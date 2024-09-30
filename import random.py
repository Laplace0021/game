import random

def select_random_option(options, weights):
    # Calculate total weight
    total_weight = sum(weights)
    
    # Normalize weights
    normalized_weights = [weight / total_weight for weight in weights]
    
    # Initialize counters
    count = 0
    count_4_star = 0
    count_5_star = 0
    
    # Randomly select options with pity system
    while True:
        selected_option = random.choices(options, weights=normalized_weights, k=1)[0]
        count += 1
        
        # Check if "5 star" is selected
        if selected_option == "5 star":
            count_5_star += 1
            if count_5_star >= 90:
                return selected_option, count
        
        # Check if "4 star" is selected
        elif selected_option == "4 star":
            count_4_star += 1
            if count_4_star >= 10:
                return selected_option, count
        
        # Print selected option each time (for demonstration)
        print(f"Selected option: {selected_option}")

# Example usage:
options = ["3 star", "4 star", "5 star"]
weights = [94.3, 5.1, 0.6]  # percentages

selected_option, count = select_random_option(options, weights)
print(f"Final selected option: {selected_option}")
print(f"Total selections until '5 star' or '4 star': {count}")
