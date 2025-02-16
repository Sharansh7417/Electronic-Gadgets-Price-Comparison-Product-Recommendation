import pickle
from flask import Flask, request, render_template
from Model_Checking import recom_function
from database_connection import search_item, recommend_info

app = Flask(__name__)



# Helper function to convert data to dictionary format
def convert_to_dict(data):
    return [
        {
            'title': item[0],
            'url': item[1],
            'image_url': item[2],
            'price': item[3],
            'rating': item[4],
            'Website': item[5],
            'category': item[6]
        }
        for item in data
    ]


@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    rec_result_dict1 = []

    # When the form is submitted (POST)
    if request.method == 'POST':
        query = request.form['query']
        # result_dict = []

        try:
            # Fetch search results from the database
            result = search_item(query)

            if result:
                result_dict = convert_to_dict(result)
                recommendations = result_dict

                # Get the recommendation based on the first result
                product_title = result_dict[0].get('title')
                print(f"Product title: {product_title}")
                row_id = recom_function(product_title)

                if row_id:
                    only_index = [i[0] for i in row_id]
                    rec_result = recommend_info(only_index)

                    if rec_result:
                        rec_result_dict1 = convert_to_dict(rec_result)
                    else:
                        rec_result_dict1 = [{"message": "No recommendations available"}]
                else:
                    rec_result_dict1 = [{"message": "Failed to generate recommendations"}]

            else:
                # If no results are found, we keep the page static with empty results
                rec_result_dict1 = [{"message": "No results found"}]

        except Exception as e:
            # If any exception occurs, just keep the page as is without changing the view
            print(f"An error occurred: {str(e)}")
            rec_result_dict1 = [{"message": "An error occurred, please try again later."}]

    # Render the template with either empty results or the last successful data
    return render_template('index1.html', recommendations=recommendations, recommended_products=rec_result_dict1)


if __name__ == '__main__':
    app.run(debug=True)
