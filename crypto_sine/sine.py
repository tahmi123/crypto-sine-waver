import numpy as np
import matplotlib.pyplot as plt

# Sample crypto price data
def sine(prices):
    crypto_prices = prices

    # Normalize prices to range [-1, 1]
    normalized_prices = 2 * (np.array(crypto_prices) - min(crypto_prices)) / (max(crypto_prices) - min(crypto_prices)) - 1

    # Apply sine wave transformation
    sine_wave_values = np.sin(normalized_prices)

    # Plot the original prices and the sine wave values
    plt.figure(figsize=(10, 6))
    #plt.plot(crypto_prices, label='Crypto Prices', marker='o')
    plt.plot(sine_wave_values, label='Sine Wave Values', linestyle='--')
    plt.xlabel('Time')
    plt.ylabel('Normalized Values')
    plt.legend()
    plt.title('Crypto Prices Normalized to Sine Wave Values')
    return plt.show()