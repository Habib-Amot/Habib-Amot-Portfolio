import { useEffect } from "react";
import more_horiz from "../../../assets/icons/more_horiz.svg"

export default function PatientNavItem({patient, isSelected, setPatient, setSelectedPatientId, id}) {
    let {profile_picture, name, gender, age} = patient;

    useEffect(() => {
        isSelected && setPatient(patient);
        // console.log(patient)
    });

    function handleClick() {
        setPatient(patient);
        setSelectedPatientId(id);
    }
    return (
        <div className={`flex items-center justify-center w-full px-2 py-4 ${isSelected ? 'bg-[#D8FCF7]' : 'bg-white'}`} onClick={handleClick}>
            <div className="patient-info flex items-center justify-between w-full bg-transparent p-0">
                <div className="patient-details flex items-center gap-4">
                    <div className="profile-image">
                        <img src={profile_picture} alt={name} className="w-12 h-12 rounded-full" />
                    </div>
                    <div className="data flex flex-col gap-1">
                        <h2 className="text-sm font-semibold">{name}</h2>
                        <p className="text-xs text-gray-500">{gender}, {age}</p>
                    </div>
                </div>
                <img src={more_horiz} alt="more options" className="more-options w-4.5 h-[3.71px] " />
            </div>
        </div>
    );
}