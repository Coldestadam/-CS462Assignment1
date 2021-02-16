import pandas as pd
import matplotlib.pyplot as plt

# A

def readData(csvFile):
	return pd.read_csv(csvFile, header=None)

# B
def mostValueCount(df, col):
	return df.loc[:, col].value_counts().index[0]

# C
def mostValueCountRecurrence(df):
	df = df.loc[df.loc[:, 0] == "recurrence-events"]
	return [mostValueCount(df, 1), mostValueCount(df, 2)]

# D
def plotRecurrencesByAge(df):
	df_recurrences = df.loc[df.loc[:, 0] == "recurrence-events"]
	df_recurrences.loc[:, 1].value_counts().plot(kind="bar", color="orange", xlabel="Age Group", ylabel="Number of Recurrences")
	plt.show()

def main():
	print("A) Reading in the Dataset")
	df = readData("breast-cancer.data")
	print(df.head())

	print("\nB) Most Common classification for the breast cancer data:")
	print(mostValueCount(df, 0))

	print("\nC) The most common value for age and menopause for patients with recurrences:")
	print(mostValueCountRecurrence(df))

	print("\nD) Plot the number of recurrences for each age group:")
	plotRecurrencesByAge(df)


if __name__ == '__main__':
	main()