import { useEffect, useState } from "react";

export default function usePatientData(patientName) {
    const [patientData, setPatientData] = useState({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchPatientData() {
            let creds = btoa('coalition:skills-test');
            const response = await fetch("https://fedskillstest.coalitiontechnologies.workers.dev", {
                method: "GET",
                headers: {
                    "Authorization": `Basic ${creds}`
                }
            });
            const data = await response.json();
            let patient = data.find((patient) => patient.name.toLowerCase() === patientName.toLowerCase());
            if (!patient) {
                setPatientData({});
                setLoading(false);
                return;
            }
            setPatientData(patient);
            setLoading(false);
        }
        fetchPatientData();
    }, [patientName]);

    return { patientData, loading };
}