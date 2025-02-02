import pandas as pd
import datetime

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

def generate_html(csv_file, output_html):
    df = pd.read_csv(f"./{csv_file}")
    
    html_content = ""
    
    for _, row in df.iterrows():
        print("new row added")
        html_content += f"""
        <div class="grid grid-cols-4">
            <div class="col-span-1 text-right pr-6 pt-4">
                <h3 class="text-2xl font-semibold capitalize">{format_date(row['Date'])}</h3>
            </div>
            <div class="col-span-3 pb-10 pl-6 border-l border-blue-500">
                <div class="relative w-4 h-4 bg-pink-500 rounded-full -left-8 -bottom-6"></div>
                <h3 class="text-2xl font-semibold capitalize">{row['Title']}</h3>
                <p class="py-4 text-gray-400">{row['Summary']}</p>
                <span class="text-sm text-gray-500">Source: <a href="{row['News1 URL']}" class="underline" target="_blank">{row['News1']}</a></span><br>
            </div>
        </div>
        """
    
    with open(output_html, "w", encoding="utf-8") as file:
        file.write(html_content)
        print(f"HTML file '{output_html}' generated successfully!")
    
generate_html("input.csv", "gen_timeline.html")
