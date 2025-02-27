Promise.myAll = function (arr) {
    return new Promise((res, rej) => {
      const result = [];
      let completed = 0;
      for (let i = 0; i < arr.length; i++) {
        const promise = arr[i];
        Promise.resolve(promise)
          .then((data) => {
            result[i] = data;
            completed++;
            if (completed === arr.length) {
              res(result);
            }
          })
          .catch((err) => rej(err));
      }
    });
  }
