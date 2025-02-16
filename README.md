# Electronic-Gadgets-Price-Comparison-Product-Recommendation
This project uses cosine similarity to create a content-based product recommendation engine by scraping product data from several e-commerce websites. The system provides customers with individualized product recommendations and the ability to compare pricing of gadgets (laptops, smartphones,tablets,smart watches) across many platforms.

## Features
-  A comparison of prices on several e-commerce websites.
-  A system for recommending products that uses content-based filtering (Cosine Similarity).
-  Information on product categories, ratings, and costs.

## Dataset Information
The dataset, which includes product details like name, price, ratings, and description, was scraped from a variety of e-commerce websites(Amazon,Flipkart,Croma,VijaySales etc)

## Data Collection and Preprocessing
This project's data was gathered through the scraping of several e-commerce websites. The data was disorganized and inconsistent since every website had a different HTML structure. To deal with this:

- HTML Parsing: From the raw HTML, BeautifulSoup was used to parse and retrieve pertinent information, like product company, categories, RAM, storage, and more.
- Data Cleaning: Resolved conflicting tags, handled missing information, and converted product pricing into a uniform format in order to clean and organize the data.
- Feature Engineering: Following data cleansing, a structured table with product attributes such as Product_name, Product_price, Product_ratings, etc. was created.

## Project Workflow


![image](https://github.com/user-attachments/assets/852611da-3349-40e1-bca0-817dac70a7b9)






