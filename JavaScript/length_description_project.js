function printDescriptionLengths(pageNumber, dataPerPage) {
  const allProductsUrl = `https://academics.newtonschool.co/api/v1/ecommerce/clothes/products?page=${pageNumber}&limit=${dataPerPage}`;
  const projectID = `ewb9qxqfh5y7`;
  const fetchAllProducts = async () => {
    return await fetch(allProductsUrl, {
      headers: {
        projectID,
      },
    });
  };
  const fetchProductsByIds = async (productId) => {
    const productUrl = `https://academics.newtonschool.co/api/v1/ecommerce/product/${productId}`;
    return await fetch(productUrl, {
      headers: {
        projectID,
      },
    });
  };
  async function abc() {
    const response = await fetchAllProducts();
    const { data } = await response.json();
    Promise.all(
      data.map(async ({ _id }) => {
        const resp = await fetchProductsByIds(_id);
        const r = await resp.json();
        return r;
      })
    ).then((res) => {
      res.map(({ data: { description } }) => console.log(description.length));
    });
  }
  abc();
}
