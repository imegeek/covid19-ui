import os
import sys
import pyfiglet
from pyfiglet import Figlet

figlet = Figlet(font="slant").renderText("Covid-19").split("\n")
max_len = len(max(figlet))

print("<" + "─" * max_len)

col = 0

for text in figlet:
	print("\33[9" + str(col) + "m" + text)
	col += 1

print("\33[0m", end="")

print("─" * max_len + ">")

def main():
	print("\33[91m• To prevent the spread of COVID-19:")
	print("\33[92m• Clean your hands often. Use soap and water, or an alcohol-based hand rub.")
	print("\33[93m• Maintain a safe distance from anyone who is coughing or sneezing.")
	print("\33[94m• Don’t touch your eyes, nose or mouth.")
	print("\33[95m• Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
	print("\33[96m• Stay home if you feel unwell.")
	print("\33[97m• If you have a fever, a cough, and difficulty breathing, seek medical attention. Call in advance.")
	print("\33[91m• Follow the directions of your local health authority.")

if __name__ == "__main__":
	main()
