import LabResultDisplay from "./ui/PatientDetail/LabResultDisplay"

const LabResults = ({currentPatient, isLoading, error}) => {
  return (
    <div className="flex flex-col gap-6 p-4 bg-white rounded-xl max-h-74 overflow-y-scroll">
      <h2 className="font-bold mb-2">Lab Results</h2>
      {
        isLoading && <p>Loading lab results...</p>
      }
      {
        error && <p>Error loading lab results. Please try again later.</p>
      }
      {
        !isLoading && !error && currentPatient.lab_results && currentPatient.lab_results.length > 0 ? (
          <div className="lab-results-list w-full h-auto flex flex-col gap-4">
            {currentPatient.lab_results.map((result, index) => (
              <LabResultDisplay key={index} resultName={result} />
            ))}
          </div>
        ) : (
          <p>No lab results available.</p>
        )
      }
    </div>
  )
}

export default LabResults
