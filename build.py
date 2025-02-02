from staticjinja import Site
import datetime
import pandas as pd

def format_date(date_str):
    # Parse the input date string
    date_obj = datetime.datetime.strptime(date_str, "%m/%d/%Y")
    
    # Get the day with proper suffix
    day = date_obj.day
    if 10 <= day % 100 <= 20:  # Special case for 11th-13th
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    
    # Format the final string
    formatted_date = date_obj.strftime(f"%B {day}{suffix}")
    return formatted_date

def get_timeline():
    df = pd.read_csv("./data/timeline.csv")
    df['Formatted Date'] = df['Date'].apply(format_date)
    return df


if __name__ == "__main__":

    site = Site.make_site(
        env_globals={
        'timeline':get_timeline(),
        },
        searchpath="src",
        outpath="docs",
        staticpaths=["static/"]
    )
    # enable automatic reloading
    site.render(use_reloader=False)