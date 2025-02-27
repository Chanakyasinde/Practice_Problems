Promise.myAllSettled = function (arr) {
    const myarr = arr.map((promise) =>
      Promise.resolve(promise)
        .then((val) => ({ status: "fulfilled", value: val }))
        .catch((err) => ({ status: "rejected", reason: err }))
    );
    return Promise.all(myarr);
  }
