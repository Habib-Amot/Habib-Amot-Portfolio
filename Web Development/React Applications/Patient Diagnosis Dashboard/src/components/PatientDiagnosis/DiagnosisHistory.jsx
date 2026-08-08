import BloodPressureChart from "./BloodPressureChart";
import BloodPressureDetailItem from "../atomic/BloodPressureInfoDisplay/BloodPressureDetailItem";
import respiratory_rate_icon from '../../assets/icons/respiratory-rate.svg'
import temperature_icon from '../../assets/icons/temperature.svg'
import heartBPM_icon from '../../assets/icons/HeartBPM.svg'

import { useState } from "react";

export default function PatientDiagnosisHistory({patientDiagnosisHistory}) {
    let [currentDiagnosisData, setCurrentDiagnosisData] = useState(patientDiagnosisHistory[0]);

    let {respiratory_rate, temperature, heart_rate} = currentDiagnosisData;

    respiratory_rate = {...respiratory_rate, bgColor: "#E0F3FA", name:"Respiratory Rate", icon:respiratory_rate_icon, unit:"Bpm"}
    temperature = {...temperature, bgColor: '#FFE6E9', name:"Temperature", icon:temperature_icon, unit:"\u00b0"+"F"}
    heart_rate = {...heart_rate, bgColor:"#FFE6F1", name:"Heart Rate", icon:heartBPM_icon, unit:"Bpm"}
    
    let _ = [respiratory_rate, temperature, heart_rate]
    return (
        <div className="flex flex-col gap-4 p-4 w-full rounded-2xl">
            <p className="text-xl font-bold">Diagnosis History</p>
            <div className="flex flex-col gap-4">
                <BloodPressureChart diagnosisHistory={patientDiagnosisHistory} setCurrentDiagnosisData={setCurrentDiagnosisData} />
                <div className="flex justify-between">
                    {_.map((item, key)=> <BloodPressureDetailItem icon={item.icon} readingName={item.name} readingValue={item.value} readingLevel={item.levels} reading_unit={item.unit} bgColor={item.bgColor} key={key}/>)}
                </div>
            </div>
        </div>
    );
}