{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.preprocessing import OneHotEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Airline</th>\n",
       "      <th>Date_of_Journey</th>\n",
       "      <th>Source</th>\n",
       "      <th>Destination</th>\n",
       "      <th>Route</th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>IndiGo</td>\n",
       "      <td>24/03/2019</td>\n",
       "      <td>Banglore</td>\n",
       "      <td>New Delhi</td>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>22:20</td>\n",
       "      <td>01:10 22 Mar</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Airline Date_of_Journey    Source Destination      Route Dep_Time  \\\n",
       "0  IndiGo      24/03/2019  Banglore   New Delhi  BLR → DEL    22:20   \n",
       "\n",
       "   Arrival_Time Duration Total_Stops Additional_Info  Price  \n",
       "0  01:10 22 Mar   2h 50m    non-stop         No info   3897  "
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_excel('./data/data.xlsx')\n",
    "df.head(1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Airline , Source , Destination"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "encoder = OneHotEncoder()\n",
    "encoded_df = pd.DataFrame(encoder.fit_transform(df[['Airline','Source','Destination']]).toarray(),columns=encoder.get_feature_names_out())\n",
    "\n",
    "df = pd.concat([df,encoded_df],axis = 1)\n",
    "\n",
    "df = df.drop(['Airline','Source','Destination'],axis = 1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Date of Journey"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Journey_date'] = df['Date_of_Journey'].str.split('/').str[0].astype(int)\n",
    "df['Journey_month'] = df['Date_of_Journey'].str.split('/').str[1].astype(int)\n",
    "df['Journey_year'] = df['Date_of_Journey'].str.split('/').str[2].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Route</th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Airline_Air Asia</th>\n",
       "      <th>Airline_Air India</th>\n",
       "      <th>Airline_GoAir</th>\n",
       "      <th>...</th>\n",
       "      <th>Source_Mumbai</th>\n",
       "      <th>Destination_Banglore</th>\n",
       "      <th>Destination_Cochin</th>\n",
       "      <th>Destination_Delhi</th>\n",
       "      <th>Destination_Hyderabad</th>\n",
       "      <th>Destination_Kolkata</th>\n",
       "      <th>Destination_New Delhi</th>\n",
       "      <th>Journey_date</th>\n",
       "      <th>Journey_month</th>\n",
       "      <th>Journey_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>BLR → DEL</td>\n",
       "      <td>22:20</td>\n",
       "      <td>01:10 22 Mar</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>2019</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CCU → IXR → BBI → BLR</td>\n",
       "      <td>05:50</td>\n",
       "      <td>13:15</td>\n",
       "      <td>7h 25m</td>\n",
       "      <td>2 stops</td>\n",
       "      <td>No info</td>\n",
       "      <td>7662</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>2019</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                   Route Dep_Time  Arrival_Time Duration Total_Stops  \\\n",
       "0              BLR → DEL    22:20  01:10 22 Mar   2h 50m    non-stop   \n",
       "1  CCU → IXR → BBI → BLR    05:50         13:15   7h 25m     2 stops   \n",
       "\n",
       "  Additional_Info  Price  Airline_Air Asia  Airline_Air India  Airline_GoAir  \\\n",
       "0         No info   3897               0.0                0.0            0.0   \n",
       "1         No info   7662               0.0                1.0            0.0   \n",
       "\n",
       "   ...  Source_Mumbai  Destination_Banglore  Destination_Cochin  \\\n",
       "0  ...            0.0                   0.0                 0.0   \n",
       "1  ...            0.0                   1.0                 0.0   \n",
       "\n",
       "   Destination_Delhi  Destination_Hyderabad  Destination_Kolkata  \\\n",
       "0                0.0                    0.0                  0.0   \n",
       "1                0.0                    0.0                  0.0   \n",
       "\n",
       "   Destination_New Delhi  Journey_date  Journey_month  Journey_year  \n",
       "0                    1.0            24              3          2019  \n",
       "1                    0.0             1              5          2019  \n",
       "\n",
       "[2 rows x 33 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.drop(['Date_of_Journey'],axis = 1)\n",
    "df.head(2) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Route"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.drop(['Route'],axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Dep_Time</th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Airline_Air Asia</th>\n",
       "      <th>Airline_Air India</th>\n",
       "      <th>Airline_GoAir</th>\n",
       "      <th>Airline_IndiGo</th>\n",
       "      <th>...</th>\n",
       "      <th>Source_Mumbai</th>\n",
       "      <th>Destination_Banglore</th>\n",
       "      <th>Destination_Cochin</th>\n",
       "      <th>Destination_Delhi</th>\n",
       "      <th>Destination_Hyderabad</th>\n",
       "      <th>Destination_Kolkata</th>\n",
       "      <th>Destination_New Delhi</th>\n",
       "      <th>Journey_date</th>\n",
       "      <th>Journey_month</th>\n",
       "      <th>Journey_year</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22:20</td>\n",
       "      <td>01:10 22 Mar</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>2019</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "  Dep_Time  Arrival_Time Duration Total_Stops Additional_Info  Price  \\\n",
       "0    22:20  01:10 22 Mar   2h 50m    non-stop         No info   3897   \n",
       "\n",
       "   Airline_Air Asia  Airline_Air India  Airline_GoAir  Airline_IndiGo  ...  \\\n",
       "0               0.0                0.0            0.0             1.0  ...   \n",
       "\n",
       "   Source_Mumbai  Destination_Banglore  Destination_Cochin  Destination_Delhi  \\\n",
       "0            0.0                   0.0                 0.0                0.0   \n",
       "\n",
       "   Destination_Hyderabad  Destination_Kolkata  Destination_New Delhi  \\\n",
       "0                    0.0                  0.0                    1.0   \n",
       "\n",
       "   Journey_date  Journey_month  Journey_year  \n",
       "0            24              3          2019  \n",
       "\n",
       "[1 rows x 32 columns]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dep time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Dep_hour'] = df['Dep_Time'].str.split(':').str[0].astype(int)\n",
    "df['Dep_min'] = df['Dep_Time'].str.split(':').str[1].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Arrival_Time</th>\n",
       "      <th>Duration</th>\n",
       "      <th>Total_Stops</th>\n",
       "      <th>Additional_Info</th>\n",
       "      <th>Price</th>\n",
       "      <th>Airline_Air Asia</th>\n",
       "      <th>Airline_Air India</th>\n",
       "      <th>Airline_GoAir</th>\n",
       "      <th>Airline_IndiGo</th>\n",
       "      <th>Airline_Jet Airways</th>\n",
       "      <th>...</th>\n",
       "      <th>Destination_Cochin</th>\n",
       "      <th>Destination_Delhi</th>\n",
       "      <th>Destination_Hyderabad</th>\n",
       "      <th>Destination_Kolkata</th>\n",
       "      <th>Destination_New Delhi</th>\n",
       "      <th>Journey_date</th>\n",
       "      <th>Journey_month</th>\n",
       "      <th>Journey_year</th>\n",
       "      <th>Dep_hour</th>\n",
       "      <th>Dep_min</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>01:10 22 Mar</td>\n",
       "      <td>2h 50m</td>\n",
       "      <td>non-stop</td>\n",
       "      <td>No info</td>\n",
       "      <td>3897</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24</td>\n",
       "      <td>3</td>\n",
       "      <td>2019</td>\n",
       "      <td>22</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1 rows × 33 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   Arrival_Time Duration Total_Stops Additional_Info  Price  Airline_Air Asia  \\\n",
       "0  01:10 22 Mar   2h 50m    non-stop         No info   3897               0.0   \n",
       "\n",
       "   Airline_Air India  Airline_GoAir  Airline_IndiGo  Airline_Jet Airways  ...  \\\n",
       "0                0.0            0.0             1.0                  0.0  ...   \n",
       "\n",
       "   Destination_Cochin  Destination_Delhi  Destination_Hyderabad  \\\n",
       "0                 0.0                0.0                    0.0   \n",
       "\n",
       "   Destination_Kolkata  Destination_New Delhi  Journey_date  Journey_month  \\\n",
       "0                  0.0                    1.0            24              3   \n",
       "\n",
       "   Journey_year  Dep_hour  Dep_min  \n",
       "0          2019        22       20  \n",
       "\n",
       "[1 rows x 33 columns]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df.drop(['Dep_Time'],axis = 1)\n",
    "df.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Arrival Time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        01:10 22 Mar\n",
       "1               13:15\n",
       "2        04:25 10 Jun\n",
       "3               23:30\n",
       "4               21:35\n",
       "             ...     \n",
       "10678           22:25\n",
       "10679           23:20\n",
       "10680           11:20\n",
       "10681           14:10\n",
       "10682           19:15\n",
       "Name: Arrival_Time, Length: 10683, dtype: object"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Arrival_Time'].str.spli"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
