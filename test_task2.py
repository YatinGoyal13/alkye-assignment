from task2 import max_profit

# Test Cases
def test_max_profit():
    # Test Case 1: Increasing trend
    prices1 = [7, 1, 5, 3, 6, 4, 9, 2, 8]
    assert max_profit(prices1) == (8, 2, 7), "Test Case 1 Failed"

    # Test Case 2: Decreasing trend
    prices2 = [9, 7, 5, 4, 3, 2, 1]
    assert max_profit(prices2) == (0, 0, 0), "Test Case 2 Failed"

    # Test Case 3: Empty list
    prices3 = []
    assert max_profit(prices3) == (0, 0, 0), "Test Case 3 Failed"

    # Test Case 4: Single price
    prices4 = [10]
    assert max_profit(prices4) == (0, 0, 0), "Test Case 4 Failed"

    # Test Case 5: Two prices
    prices5 = [10, 20]
    assert max_profit(prices5) == (10, 1, 2), "Test Case 5 Failed"

    print("All test cases passed successfully.")

# Run the test cases
if __name__ == "__main__":
    test_max_profit()
