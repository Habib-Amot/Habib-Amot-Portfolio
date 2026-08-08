import './App.css'
import NavBar from './components/Bar/NavBar'
import SideBar from './components/Bar/SideBar'
import PatientDiagnosis from './components/PatientDiagnosis'
import PatientDetails from './components/PatientDetails'
import LabResults from './components/LabResults'
import getPatientData from './utils/patient-data';
import { useEffect, useState } from 'react'
import DiagnosticList from './components/DiagnosticList'

function App() {
  let [patients, setPatients] = useState({})
  let [isLoading, setIsLoading] = useState(true)
  let [error, setError] = useState(false)
  let [currentPatient, setCurrentPatient] = useState({})

  useEffect(()=>{
    let fetchData = async ()=>{
      try{
        setIsLoading(true)
        let response = await getPatientData()
        let data = await response.json()
        setPatients(data)  // Set the fetched patient data to state
      } 
      catch {
        setError(true)
      } 
      finally {
        setIsLoading(false)
      }
    }
    fetchData()
  }, [])

  return (
    <div className='bg-[#F6F7F8] w-full h-full font-manrope p-4 flex flex-col gap-8'>
      <NavBar/>
      <div className="w-full h-auto grid grid-cols-[1fr_2fr_1fr] gap-8">
        <SideBar patients={patients} setPatient={setCurrentPatient} isLoading={isLoading} error={error}/>
        <div className="diag flex flex-col gap-4">
          <PatientDiagnosis currentPatient={currentPatient} isLoading={isLoading} error={error}/>
          <DiagnosticList currentPatient={currentPatient} isLoading={isLoading} error={error}/>
        </div>
        <div className="details flex flex-col gap-4">
          <PatientDetails currentPatient={currentPatient} isLoading={isLoading} error={error}/>
          <LabResults currentPatient={currentPatient} isLoading={isLoading} error={error}/>
        </div>
      </div>
    </div>
  )
}

export default App
