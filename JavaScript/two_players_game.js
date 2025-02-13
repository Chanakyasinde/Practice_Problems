function findWinner(scores) {
  for (let i=0; i<scores.length; i++){
    if (i%2==0){
      if (scores[i]<0){
        return "Arun";
      }
    } else {
      if (scores[i]<0){
        return "Naman";
      }
    }
  }
}
