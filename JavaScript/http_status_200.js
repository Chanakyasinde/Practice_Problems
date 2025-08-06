async function checkStatus(url) {
  try {
    const response = await fetch(url);
    if (response.ok) {
      return "Success!";
    } else {
      return `Error: Received status code ${response.status}`;
    }
  } catch (error) {
    console.error("Network error");
    return "Network error";
  }
}
