import { useState } from 'react'
import { Line } from 'react-chartjs-2';
import { LuChevronDown } from 'react-icons/lu';
import bloodPressureOptions  from '../../config/bloodPressureOptions';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend} from 'chart.js';
import SystolicBloodPressureInfoDisplay, { DiastolicBloodPressureInfoDisplay } from '../atomic/BloodPressureInfoDisplay/BloodPressureInfoDisplay';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export default function BloodPressureChart({diagnosisHistory, setCurrentDiagnosisData}) {
    let [systolicInfo, setSystolicInfo] = useState({value: 0, level: ""});
    let [diastolicInfo, setDiastolicInfo] = useState({value: 0, level: ""});

    // let lastSixMonthHistory = null;
    let systolicData = diagnosisHistory.filter((diagnosis)=>Object.hasOwn(diagnosis.blood_pressure, 'systolic')).map((diagnosis)=>{
        return {label: diagnosis.month.substring(0, 3)+" "+diagnosis.year, pressure_type: "systolic", value: diagnosis.blood_pressure.systolic.value, diagnosis: diagnosis}
    });

    let diastolicData = diagnosisHistory.filter((diagnosis)=>Object.hasOwn(diagnosis.blood_pressure, 'diastolic')).map((diagnosis)=>{
        return {label: diagnosis.month.substring(0, 3)+" "+diagnosis.year, pressure_type: "diastolic", value: diagnosis.blood_pressure.diastolic.value, diagnosis: diagnosis}
    });
    let data = {
        labels: diagnosisHistory.map((diagnosis) => diagnosis.month.substring(0, 3)+" "+diagnosis.year),
        datasets:[
            {
                label: "",
                data: systolicData,
                borderColor: "#C26EB4",
                pointBackgroundColor: "#E66FD2",
                parsing:{
                    xAxisKey: 'label',
                    yAxisKey: 'value'
                }
            },
            {
                label: "",
                data: diastolicData,
                borderColor: "#7E6CAB",
                pointBackgroundColor: "#8C6FE6",
                parsing:{
                    xAxisKey: 'label',
                    yAxisKey: 'value'
                }
            }
        ]
    }
    let options = bloodPressureOptions(setSystolicInfo, setDiastolicInfo, setCurrentDiagnosisData);
    return (
        <div className='w-full h-auto bg-[#F4F0FE] p-4 rounded-3xl flex gap-10'>
            <div className="main">
                <div className="header flex justify-between items-center mb-2">
                    <h2 className='font-bold'>Blood pressure</h2>
                    <div className="flex items-center">
                        <p className='text-sm'>last 6 months </p>
                        <LuChevronDown/>
                    </div>
                </div>
                <div className="line h-60 w-104.25 flex justify-between">
                    <Line data={data} options={options}/>
                </div>
            </div>
            <div className="divide-gray-200 divide-y-2">
                <SystolicBloodPressureInfoDisplay readings={systolicInfo}/>
                <DiastolicBloodPressureInfoDisplay readings={diastolicInfo}/>
            </div>
        </div>
    )
}