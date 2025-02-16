function searchProducts() {
    const query = document.getElementById('searchInput').value;

    if (query === '') {
        alert('Please enter a search term.');
        return;
    }

    // Fetch data from Flask API
    fetch(`/search?query=${query}`)
        .then(response => response.json())
        .then(data => {
            let resultsHTML = '';

            // Dynamically create product blocks for each result
            if (data.length > 0) {
                data.forEach(product => {
                    resultsHTML += `
                        <div class="product-card">
                            <h3>${product.title}</h3>
                            <p>Price: ₹${product.price}</p>
                            <p>Rating: ${product.rating}</p>
                        </div>
                    `;
                });
            } else {
                resultsHTML = '<p>No products found.</p>';
            }

            // Insert the product blocks into the HTML
            document.getElementById('results').innerHTML = resultsHTML;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('results').innerHTML = '<p>Error fetching data. Please try again later.</p>';
        });
}
