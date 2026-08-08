
export default function bloodPressureOptions(setSystolic, setDiastolic, setCurrentDiagnosisData) {
    return {
            onClick: (event, elements, chart) => {
                if(elements.length > 0){
                    const { datasetIndex, index } = elements[0];
                    const dataset = chart.data.datasets[datasetIndex];
                    const dataPoint = dataset.data[index];
                    setSystolic({value: dataPoint.diagnosis.blood_pressure.systolic.value, level: dataPoint.diagnosis.blood_pressure.systolic.levels})
                    setDiastolic({value: dataPoint.diagnosis.blood_pressure.diastolic.value, level: dataPoint.diagnosis.blood_pressure.diastolic.levels})
                    setCurrentDiagnosisData(dataPoint.diagnosis)
            }
        },
        elements:{
            line:{
                borderWidth: 1,
                tension: 0.4,
            },
            point:{
                radius: 3,
            }
        },
        maintainAspectRatio: false,
        responsive: true,
        plugins:{
            legend: {
                display: false
            }
        },
        scales: {
            y: {
                min: 60,
                max: 180,
                ticks: {
                    stepSize: 20,
                    autoSkip: false
                },
                
            },
            x: {
                grid:{
                    display: false,
                },
                ticks:{
                    maxRotation:0,
                    minRotation:0,
                    font:{
                        size:8
                    }
                }
            }
        },
    }
}