"""

This is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. It is
distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the code.  If not, see <http://www.gnu.org/licenses/>.

File name: 	EDA_Titanic.py
Created: 8th December 2022
Author: Nigel Cooksley BEng PGCE

Contact: njcooksley@live.co.uk
LinkedIn Profile: www.linkedin.com/in/nigel-cooksley-bristol
github profile: github.com/jimbounce

"""

import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def main():
    """
    Kaggle competition on Titanic dataset. Team from Bristol Data Science and ML.

    """

df = pd.read_csv("train.csv")

pd.set_option('display.width', 1200)  # These two lines so all columns are printed
pd.set_option('display.max_columns', 100)

print(df.describe(), "/n")
print(df.info(verbose=True), "\n")
print(df.columns, "\n")    # Lists column headings

# Finding the number of children with just a nanny (age <18 and Parch = 0 (no relatives))
#print(df.loc[(df["Parch"].isin([0])) & (df["Age"]==80)])

# Did the eldest passenger (aged 80) survive?
print(df.loc[(df["Age"]==80)])     # yes!

# #Dropping columns to create a submission csv
# df.drop(["Corporate Contributors","Corporate Author", "Engraver"], axis =1, inplace = True)        #Works, woohoo
# #                                     axis = 1 cols, axis= 0 is rows.        #inplace true for removal
# print("printing df_info", df.info())    #checking if col deletion worked