import numpy as np
import pandas as pd
def basic(df):
    print("*"*50,"\nRow {} Column  {}". format(   str(df.shape[0])  , str(df.shape[1])) )
    
    print("*"*50,"\nInformation \n",df.info)
    
    print("*"*50,"\nDescription for numerical \n", df.describe())
    
    print("*"*50,"\nDescription for object \n", df.describe(include=object))
    
    null_df=pd.DataFrame(df.isnull().sum())
    null_df.columns=['Count']
    print("*"*50,"\nThe Null keys\n\n", null_df)
    
    print("*"*50,"\nThe Null values\n\n",null_df[null_df['Count'] > 0])
  
    df_numeric=df.select_dtypes(exclude='object')
    df_num_cols=df_numeric.columns
    
    for c in df_num_cols:
        print(c)
        print(iqr_outliers(df[c]))
        print('-'*100)
    
def iqr_outliers(num_array):
    """
    Finds outliers based on IQR method
    Params:
    -------
    num_arrar: numpy array or list
    Returns:
    --------
    List of outliers if present
    """
    # Find 25th percentile / q1
    q1 = np.nanpercentile(num_array, 25)
    # Find 25th percentile / q1
    q3 = np.nanpercentile(num_array, 75)
    # Find IQR
    iqr = q3 - q1
    # Define upper and lower limits for outlier detection
    upper_limit = q3 + (1.5 * iqr)
    lower_limit = q1 - (1.5 * iqr)
    return [num for num in num_array if num > upper_limit or num < lower_limit]

if __name__ == "__main__":
    data=pd.read_csv('titanic.csv')
    df=pd.DataFrame(data)
    basic(df)
    