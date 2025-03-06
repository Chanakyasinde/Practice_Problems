const updatePost = (url, headers, body) => {
  return fetch(url, {
    headers,
    body,
    method: "PUT",
  });
};
