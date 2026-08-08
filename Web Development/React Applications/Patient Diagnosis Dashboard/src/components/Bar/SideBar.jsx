import { useState } from "react";
import search from "../../assets/icons/search.svg";
import PatientNavItem from "../atomic/Nav/PatientNavItem";

export default function SideBar({patients, setPatient, isLoading, error}) {
    let [selectedPatientId, setSelectedPatientId] = useState(4);

    return (
        <div className="py-3 px-4 rounded-2xl bg-white h-full max-w-100 max-h-261.25 overflow-y-scroll">
            <div className="flex justify-between items-center px-2">
                <h1 className="text-2xl font-extrabold">Patients</h1>
                <img src={search} alt="search" className="w-4.5 h-4.5" />
            </div>
            {error ? <p className="text-red-500 mt-4">Error fetching patient data.</p> : isLoading ? <p className="mt-4">Loading...</p> : patients.length === 0 ? <p className="mt-4">No patients available.</p> :
                <div className="mt-4 flex flex-col">
                    {patients.map((patient, index) => (
                        <PatientNavItem key={index} 
                        patient={patient} id={index} isSelected={selectedPatientId === index} setSelectedPatientId={setSelectedPatientId} setPatient={setPatient}
                    />
                    ))}
                </div>
            }
        </div>
    )
}