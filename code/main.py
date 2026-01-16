import  pandas as pd

if __name__ == "__main__":
    dfadult = pd.read_csv("data/adult.data")
    dfadult.info()
