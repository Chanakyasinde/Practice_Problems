 function double(value) {
    return new Promise((res) => {
        res(value*2)
    })
}

function addTen(value) {
    return new Promise((res) => {
        res(value+10)
    })
}

function multiplyByThree(value) {
    return new Promise((res) => {
        res(value*3)
    })
}

double(value)
    .then(addTen)
    .then(multiplyByThree)
    .then((result) => {
        console.log(result)
    })
    .catch((error) => {
        console.log(error)
    })
