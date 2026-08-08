/* this is a simple grade calculator function
the function takes student score then return the grade for that student
invalid and negative scores are simply handled and rejected by the function
 */

function calculateGrade(score) {
    if (score < 0 || score > 100 || score === undefined){
        return "F"; // this handles situations where the score is negative or undefined
    }else{
        if (score >= 90) {
            return "A";
        }
        else if (score >= 80) {
            return "B";
        }
        else if (score >= 70) {
            return "C";
        }
        else if (score >= 60) {
            return "D";
        }
        else if (score >= 50) {
            return "E";
        }
        else {
            return "F";
        }
    }
}
// this function takes an array of student scores and returns the number of students in each grade category
// it also handles invalid inputs and returns an error message
// by passing the group_score parameter, it allows the funnction to return students grades in each grade category
// the function also handles the case where the input is not an array or is empty
function classroomGrade(students_scores, group_score=false){
    if(typeof students_scores !== "object" || students_scores.length === 0){
        return "Invalid input, please enter an array of student scores";
    }else{
        let grades = group_score ? {A:[], B:[], C:[], D:[], E:[], F:[]} : {A: 0, B: 0, C: 0, D: 0, E:0, F: 0};
        students_scores = students_scores.filter(score => score !== undefined && score >= 0 && score <= 100);
        if(students_scores.length === 0){
            return "No valid scores found";
        }
        for(let score of students_scores){
            group_score ? grades[calculateGrade(score)].push(score) : grades[calculateGrade(score)]++;
        }
        return grades;
    }
}

let startTime = performance.now();
classroomGrade([90, 85, 78, 92, 88, 76, 95, 89, 67, 72, 35, 30, 50, 45, undefined, 0, 100, 450, 90]); 
let endTime = performance.now();
console.log("Execution time: " + (endTime - startTime) + " milliseconds");