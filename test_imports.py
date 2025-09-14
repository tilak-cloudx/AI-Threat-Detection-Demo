"""
Quick sanity check for deployment.

Run this with: python test_imports.py
If it runs without errors, your environment is healthy.
"""

try:
    import streamlit
    import pandas
    import numpy
    import matplotlib
    import plotly
    import joblib
    import wikipedia
    import gtts
    import altair

    print("✅ All libraries imported successfully!")

except Exception as e:
    print("❌ Import error:", e)
    raise
