import pandas as pd

def main():
    data = pd.read_csv('data.csv')


if __name__ == "__main__":
    main()
else:
    print("This script is intended to be run directly, not imported.")