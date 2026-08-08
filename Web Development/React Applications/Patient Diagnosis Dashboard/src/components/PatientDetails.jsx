import PatientInfo from "./atomic/InfoDisplay/PatientInfo";
import femaleIcon from "../assets/icons/FemaleIcon.svg";
import phoneIcon from "../assets/icons/PhoneIcon.svg";
import birthIcon from "../assets/icons/BirthIcon.svg";
import insuranceIcon from "../assets/icons/InsuranceIcon.svg";

export default function PatientDetails({ currentPatient, isLoading, error }) {
    return (isLoading || error) ? (
        <div className="flex flex-col gap-4 p-4 bg-white rounded-2xl grow-2">
            {isLoading && <p>Loading patient details...</p>}
            {error && <p>Error loading patient details. Please try again later.</p>}
        </div>
    ) : (
        <div className="flex flex-col gap-12 pt-12 pb-5 bg-white rounded-2xl">
            <div className="profile-section flex flex-col items-center gap-2 w-full h-auto">
                <div className="img *:w-38 *:h-38 rounded-full overflow-hidden">
                    <img src={currentPatient.profile_picture} alt="Profile" className="w-full rounded-full" />
                </div>
                <div className="info">
                    <h2 className="text-xl font-bold">{currentPatient.name}</h2>
                </div>
            </div>
            <div className="flex flex-col gap-4 px-6">
                <PatientInfo ico={birthIcon} header="Date of birth" value={currentPatient.date_of_birth}/>
                <PatientInfo ico={femaleIcon} header="Gender" value={currentPatient.gender}/>
                <PatientInfo ico={phoneIcon} header="Contact info." value={currentPatient.phone_number}/>
                <PatientInfo ico={phoneIcon} header="Emergency Contacts." value={currentPatient.emergency_contact}/>
                <PatientInfo ico={insuranceIcon} header="Insurance Provider" value={currentPatient.insurance_type}/>
            </div>
            <button className="w-fit h-fit px-8 py-3 flex items-center justify-center self-center text-sm rounded-3xl text-gray-700 bg-green-400 font-semibold capitalize">
                show all information
            </button>
        </div>
    )
}