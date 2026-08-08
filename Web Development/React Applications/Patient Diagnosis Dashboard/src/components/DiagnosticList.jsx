import PatientDetailDisplay from "./ui/PatientDetail/PatientDetailDisplay"

const DiagnosticList = ({currentPatient, isLoading, error}) => {
  return (
    isLoading || error || Object.keys(currentPatient).length == 0 ? <div>
        <p>data is loading or no internet connection</p>
    </div> :
    <div className="bg-white w-full h-auto rounded-2xl p-6 flex flex-col gap-6 max-h-87.25 overflow-y-scroll">
      <h2 className="font-bold mb-2">Diagnostics List</h2>
      <div className="grid grid-cols-[1.5fr_2fr_1fr] text-xs w-full h-12 rounded-md overflow-hidden px-3 bg-gray-100">
        <p className=" capitalize flex items-center w-full h-full font-semibold">problem/diagnosis</p>
        <p className=" capitalize flex items-center w-full h-full font-semibold">description</p>
        <p className=" capitalize flex items-center w-full h-full font-semibold">status</p>  
      </div>
        {
          currentPatient.diagnostic_list.map((item, index) => <PatientDetailDisplay key={index} name={item.name} description={item.description} status={item.status}/>)
        }
    </div>
  )
}

export default DiagnosticList
