function repeatWithDelay(count) {
  let executionCount = 0;
  let set_interval = setInterval(()=> {
    executionCount++;
    console.log("Interval has been executed " + executionCount + " time(s)");
    if (executionCount === count) {
      clearInterval(set_interval);
    }
  }, 1000)
  setTimeout(()=> {
    console.log("Interval execution stopped")
  },(count+1)*1000)
}
