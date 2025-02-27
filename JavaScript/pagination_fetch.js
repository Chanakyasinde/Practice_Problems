async function fetchProducts(url, pageNumber) {
    // Function Code
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const products = await response.json();
    // Calculate start and end index for pagination
    const productsPerPage = 5;
    const startIndex = (pageNumber - 1) * productsPerPage;
    const endIndex = startIndex + productsPerPage;
    // Return products for the requested page
    return products.slice(startIndex, endIndex);
  }
