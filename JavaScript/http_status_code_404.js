function checkFor404(apiUrl) {
  const validRoutes = [
    "https://api.test.com/users",
    "https://api.test.com/weather",
    "https://api.test.com/products",
    "https://api.test.com/books",
  ];

  if (!validRoutes.includes(apiUrl)) {
    return Promise.resolve("Invalid route");
  }

  return fetch(apiUrl)
    .then((response) => {
      if (response.status === 404) {
        return "Not Found";
      } else {
        return "OK Found";
      }
    })
    .catch(() => {
      // If a network error occurs, you could also return a fallback if needed
      return "Not Found";
    });
}
