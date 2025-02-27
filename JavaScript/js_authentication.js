function authenticateUser(username, password, users)
{
return new Promise((resolve,reject)=> {
    setTimeout(()=> {
        if (users[username] && users[username] === password) {
        resolve(`Login successful for user: ${username}`);
      } else {
        reject("Authentication failed. Invalid username or password.");
      }
    },3000)
})
}
