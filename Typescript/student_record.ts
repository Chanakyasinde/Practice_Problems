class StudentRecord {
  private score: number;

  constructor(initialScore: number) {
    // TODO
    if (initialScore < 0) throw new Error("Invalid initial score")
    this.score = initialScore;
  }

  addMarks(marks: number): void {
    // TODO
    if (marks < 0 || typeof marks !== "number" || isNaN(marks)) {
        console.log("Invalid marks");
    }else {
        this.score += marks
    }
  }

  deductMarks(marks: number): void {
    // TODO
    if (marks < 0 || typeof marks !== "number" || isNaN(marks)) {
        console.log("Invalid marks");
    } else if (marks > 0 && this.score-marks < 0){
        
    }
    else {
        this.score -= marks
    }
  }

  getScore(): number {
    // TODO
    return this.score;
  }
}
