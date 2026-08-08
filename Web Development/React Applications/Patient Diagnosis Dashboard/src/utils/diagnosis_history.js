function sortDiagnosisHistoryByDate(patientData){
    // console.log(patientData)
    return patientData.diagnosis_history.sort((previousHistory, currentHistory)=>{
        return new Date(`${previousHistory.month + "," + previousHistory.year}`) - new Date(`${currentHistory.month + "," + currentHistory.year}`)
    })
}


export {sortDiagnosisHistoryByDate}