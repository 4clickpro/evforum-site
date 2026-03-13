import os
import time
import subprocess
import random
from datetime import datetime

KEYWORDS = [
    "Electric bike for commuting",
    "Best electric mountain bikes",
    "Electric bikes for seniors",
    "Cheap electric bikes",
    "Fat tire electric bikes",
    "Electric cargo bikes",
    "Electric bike maintenance tips",
    "How fast do electric bikes go",
    "Electric bike range guide",
    "Electric bike for hunting"
]

def update_index(keyword, filename):
    index_path = "index.html"
    if not os.path.exists(index_path):
        return
    with open(index_path, "r") as f:
        content = f.read()
    
    card_html = f"""
            <div class="card">
                <div class="badge" style="background: #fef08a; color: #854d0e;">Blog Post</div>
                <h3>{keyword}</h3>
                <p style="margin-bottom: 1rem; color: #64748b; font-size: 0.9rem;">Read our latest guide on {keyword}...</p>
                <a href="/{filename}" class="btn-green">Read Full Guide</a>
                <a href="https://shop.theelectricbikesuperstore.com" class="btn-blue" target="_blank">Shop eBikes</a>
            </div>"""

    if '<div class="grid">' in content:
        content = content.replace('<div class="grid">', f'<div class="grid">\n{card_html}', 1)
        with open(index_path, "w") as f:
            f.write(content)

def generate_post(keyword):
    slug = keyword.lower().replace(" ", "-")
    filename = f"{slug}.html"
    
    style = """<style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1, h2, h3 { color: #333; }
        .btn-green { display: inline-block; padding: 10px 20px; background-color: #28a745; color: white; text-decoration: none; border-radius: 5px; margin-right: 10px; font-weight: bold; }
        .btn-blue { display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; }
        .buttons { margin: 30px 0; text-align: center; }
    </style>"""

    buttons_html = f"""
    <div class="buttons">
        <a href="https://shop.theelectricbikesuperstore.com" class="btn-green">Shop {keyword} Now</a>
        <a href="https://shop.theelectricbikesuperstore.com" class="btn-blue">View All Electric Bikes</a>
    </div>"""

    template_1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Top 5 Reasons why {keyword.lower()} is the right choice for you.">
    <title>Top 5 Reasons to Choose: {keyword}</title>
    {style}
</head>
<body>
    <h1>Top 5 Reasons to Choose: {keyword}</h1>
    <p>If you are looking for an <strong>{keyword.lower()}</strong>, you are joining a growing trend. Electric bikes are revolutionizing the way we travel, explore, and commute.</p>
    
    <ol>
        <li><strong>Eco-Friendly:</strong> Reduce your carbon footprint with zero emissions.</li>
        <li><strong>Cost-Effective:</strong> Save money on gas, parking, and maintenance compared to a car.</li>
        <li><strong>Health Benefits:</strong> Stay active while minimizing physical strain.</li>
        <li><strong>Convenience:</strong> Avoid traffic jams and find parking easily.</li>
        <li><strong>Fun:</strong> Enjoy the thrill of the ride with added motor assistance.</li>
    </ol>
    
    {buttons_html}
    
    <h2>Conclusion</h2>
    <p>Whether you are an experienced rider or a beginner, an {keyword.lower()} is a fantastic investment. Explore our top picks today!</p>
</body>
</html>"""

    template_2 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Learn how to choose the best {keyword.lower()} for your lifestyle.">
    <title>How to Choose the Best {keyword}</title>
    {style}
</head>
<body>
    <h1>How to Choose the Best {keyword}</h1>
    <p>Finding the right <strong>{keyword.lower()}</strong> can be overwhelming. This guide will help you make an informed decision.</p>
    
    <h2>Determine Your Needs</h2>
    <p>Consider how you will use the e-bike. Will you use it for daily commuting, off-road adventures, or leisurely weekend rides? Your primary use case will dictate the type of e-bike you should look for.</p>
    
    <h2>Consider the Motor and Battery</h2>
    <p>The motor power and battery capacity are crucial factors. A more powerful motor and larger battery will provide better performance and range but will also add weight and cost.</p>
    
    {buttons_html}
    
    <h2>Test Ride</h2>
    <p>Whenever possible, test ride different models to see which one feels the most comfortable and suits your riding style.</p>
</body>
</html>"""

    template_3 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="The ultimate buyer's guide to finding the perfect {keyword.lower()}.">
    <title>Ultimate Buyer's Guide: {keyword}</title>
    {style}
</head>
<body>
    <h1>Ultimate Buyer's Guide: {keyword}</h1>
    <p>Welcome to the ultimate buyer's guide for <strong>{keyword.lower()}</strong>. Here, we break down everything you need to know before making a purchase.</p>
    
    <h2>Key Features to Look For</h2>
    <ul>
        <li><strong>Battery Range:</strong> Ensure it covers your typical routes without needing a recharge.</li>
        <li><strong>Motor Type:</strong> Hub motors vs. mid-drive motors each have their pros and cons.</li>
        <li><strong>Brakes:</strong> Reliable braking power is essential for safety, especially at higher speeds.</li>
    </ul>
    
    {buttons_html}
    
    <h2>Budget Considerations</h2>
    <p>Set a realistic budget, but remember that investing a bit more upfront can often save you money on maintenance and repairs in the long run.</p>
</body>
</html>"""

    template_4 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Frequently asked questions about {keyword.lower()}.">
    <title>FAQ: {keyword}</title>
    {style}
</head>
<body>
    <h1>Frequently Asked Questions: {keyword}</h1>
    <p>Got questions about <strong>{keyword.lower()}</strong>? We've got answers.</p>
    
    <h2>How fast can an {keyword.lower()} go?</h2>
    <p>Most e-bikes are restricted to a certain speed (usually around 20-28 mph) depending on local laws and the bike's class.</p>
    
    <h2>Do I need a license to ride one?</h2>
    <p>In most places, no. However, regulations vary, so it's always best to check your local laws.</p>
    
    {buttons_html}
    
    <h2>How long does the battery last?</h2>
    <p>Battery life depends on the capacity, the level of assist you use, and the terrain. Typically, you can expect anywhere from 20 to 50+ miles per charge.</p>
</body>
</html>"""

    templates = [template_1, template_2, template_3, template_4]
    html_content = random.choice(templates)

    with open(filename, "w") as f:
        f.write(html_content)
    
    update_index(keyword, filename)
    
    return filename

def main():
    # Ensure working directory is correct
    os.chdir("/home/ubuntu/.openclaw/workspace/evforum-site")

    # First post must be "Electric bike for hunting"
    first_keyword = "Electric bike for hunting"
    print(f"Generating first post: {first_keyword}")
    
    filename = generate_post(first_keyword)
    
    # Git add, commit, push
    subprocess.run(["git", "add", filename, "index.html"], check=True)
    subprocess.run(["git", "commit", "-m", f"Add SEO post: {first_keyword}"], check=True)
    subprocess.run(["git", "push"], check=True)
    
    print("First post generated, committed, and pushed successfully.")
    
    # Continuous loop for other keywords
    while True:
        time.sleep(3600)  # 1 hour delay
        next_keyword = random.choice(KEYWORDS)
        print(f"[{datetime.now()}] Generating new post: {next_keyword}")
        
        fname = generate_post(next_keyword)
        
        try:
            subprocess.run(["git", "add", fname, "index.html"], check=True)
            subprocess.run(["git", "commit", "-m", f"Add SEO post: {next_keyword}"], check=True)
            subprocess.run(["git", "push"], check=True)
            print(f"Successfully published: {next_keyword}")
        except Exception as e:
            print(f"Error publishing {next_keyword}: {e}")

if __name__ == "__main__":
    main()
