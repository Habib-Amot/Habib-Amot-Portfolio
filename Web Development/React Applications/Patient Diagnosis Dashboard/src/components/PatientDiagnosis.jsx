import PatientDiagnosisHistory from "./PatientDiagnosis/DiagnosisHistory";
import { sortDiagnosisHistoryByDate } from "../utils/diagnosis_history";

export default function PatientDiagnosis({isLoading, currentPatient}) {
    let sortedPatientDiagnosisHistory = null;
    if(Object.keys(currentPatient).length > 0 && !isLoading){
        sortedPatientDiagnosisHistory = sortDiagnosisHistoryByDate(currentPatient);
    }
    return (
        <div className="flex flex-col gap-4 p-4 bg-white rounded-2xl grow-1.5d">
            <div>
                {
                isLoading || sortedPatientDiagnosisHistory == null ? "Loading..." : sortedPatientDiagnosisHistory.length > 0 ? <PatientDiagnosisHistory patientDiagnosisHistory={sortedPatientDiagnosisHistory} /> : "No diagnosis available"
                }
            </div>
        </div>
    )
}