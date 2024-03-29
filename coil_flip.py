"""
    name: coin_flip.py
    author: Jessica Soler
    created: 3/28/24
    assignment: 7.4 OOP Tutorial
    puprose: create 3 Coin objects
"""

# import coin class
import coin

def main():
    # create three objects from the Coin class
    coin_1 = coin.Coin()
    coin_2 = coin.Coin()
    coin_3 = coin.Coin()
    
    # display the side of each coin that is facing up
    print("\nI have three coins with these sides up: ")
    print(coin_1.sideup)
    print(coin_2.sideup)
    print(coin_3.sideup)
    print()
    
    # toss the coin
    print("I am flipping the coins...")
    print()
    coin_1.toss()
    coin_2.toss()
    coin_3.toss()
    
    # display the side of each coin that is facing up
    print("Here is how the coins landed:")
    print(coin_1.sideup)
    print(coin_2.sideup)
    print(coin_3.sideup)
    print()
    
# call the main function
if __name__ == "__main__":
    main()