import streamlit as st
import pandas as pd

df = pd.read_csv("athlete_events.csv")
regeion_df = pd.read_csv("noc_regions.csv")


def preprocess(df,regeion_df):

    #filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # Merge with region df
    df = df.merge(regeion_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    #One hot encoding
    dm = pd.get_dummies(df['Medal'], dtype=int)
    df = pd.concat([df, dm], axis=1)
    return df
