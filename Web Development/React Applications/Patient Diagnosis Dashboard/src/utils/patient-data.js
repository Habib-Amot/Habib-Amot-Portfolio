export default function getPatientData(){
    let patientsEndpoint = "https://fedskillstest.coalitiontechnologies.workers.dev";
    let [username, password] = ["coalition", "skills-test"];

    let creds = btoa(`${username}:${password}`);
    return fetch(patientsEndpoint, {
        method: "GET",
        headers: {
            "Authorization": `Basic ${creds}`,
        }
    })

}

/* 
[
  {
    "name": "Emily Williams",
    "gender": "Female",
    "age": 18,
    "profile_picture": "https://fedskillstest.ct.digital/1.png",
    "date_of_birth": "2006-08-19",
    "phone_number": "(711) 984-6696",
    "emergency_contact": "(680) 653-9512",
    "insurance_type": "Premier Auto Corporation",
    "diagnosis_history": [
      {
        "month": "March",
        "year": 2024,
        "blood_pressure": {
          "systolic": {
            "value": 163,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 95,
            "levels": "Normal"
          }
        },
        "heart_rate": {
          "value": 79,
          "levels": "Lower than Average"
        },
        "respiratory_rate": {
          "value": 27,
          "levels": "Normal"
        },
        "temperature": {
          "value": 103,
          "levels": "Higher than Average"
        }
      },
      {
        "month": "February",
        "year": 2024,
        "blood_pressure": {
          "systolic": {
            "value": 151,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 120,
            "levels": "Normal"
          }
        },
        "heart_rate": {
          "value": 88,
          "levels": "Normal"
        },
        "respiratory_rate": {
          "value": 27,
          "levels": "Normal"
        },
        "temperature": {
          "value": 99,
          "levels": "Normal"
        }
      },
      {
        "month": "January",
        "year": 2024,
        "blood_pressure": {
          "systolic": {
            "value": 168,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 77,
            "levels": "Lower than Average"
          }
        },
        "heart_rate": {
          "value": 82,
          "levels": "Normal"
        },
        "respiratory_rate": {
          "value": 17,
          "levels": "Normal"
        },
        "temperature": {
          "value": 97,
          "levels": "Normal"
        }
      },
      {
        "month": "December",
        "year": 2023,
        "blood_pressure": {
          "systolic": {
            "value": 158,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 92,
            "levels": "Normal"
          }
        },
        "heart_rate": {
          "value": 60,
          "levels": "Lower than Average"
        },
        "respiratory_rate": {
          "value": 21,
          "levels": "Normal"
        },
        "temperature": {
          "value": 99,
          "levels": "Normal"
        }
      },
      {
        "month": "November",
        "year": 2023,
        "blood_pressure": {
          "systolic": {
            "value": 117,
            "levels": "Normal"
          },
          "diastolic": {
            "value": 95,
            "levels": "Normal"
          }
        },
        "heart_rate": {
          "value": 100,
          "levels": "Normal"
        },
        "respiratory_rate": {
          "value": 21,
          "levels": "Normal"
        },
        "temperature": {
          "value": 103,
          "levels": "Higher than Average"
        }
      },
      {
        "month": "October",
        "year": 2023,
        "blood_pressure": {
          "systolic": {
            "value": 115,
            "levels": "Normal"
          },
          "diastolic": {
            "value": 80,
            "levels": "Lower than Average"
          }
        },
        "heart_rate": {
          "value": 63,
          "levels": "Lower than Average"
        },
        "respiratory_rate": {
          "value": 14,
          "levels": "Normal"
        },
        "temperature": {
          "value": 100,
          "levels": "Normal"
        }
      },
      {
        "month": "September",
        "year": 2023,
        "blood_pressure": {
          "systolic": {
            "value": 133,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 68,
            "levels": "Lower than Average"
          }
        },
        "heart_rate": {
          "value": 91,
          "levels": "Normal"
        },
        "respiratory_rate": {
          "value": 13,
          "levels": "Normal"
        },
        "temperature": {
          "value": 99,
          "levels": "Normal"
        }
      },
      {
        "month": "August",
        "year": 2023,
        "blood_pressure": {
          "systolic": {
            "value": 149,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 70,
            "levels": "Lower than Average"
          }
        },
        "heart_rate": {
          "value": 69,
          "levels": "Lower than Average"
        },
        "respiratory_rate": {
          "value": 14,
          "levels": "Normal"
        },
        "temperature": {
          "value": 100,
          "levels": "Normal"
        }
      },
      {
        "month": "July",
        "year": 2023,
        "blood_pressure": {
          "systolic": {
            "value": 165,
            "levels": "Higher than Average"
          },
          "diastolic": {
            "value": 95,
            "levels": "Normal"
          }
        },
        "heart_rate": {
          "value": 71,
          "levels": "Lower than Average"
        },
        "respiratory_rate": {
          "value": 14,
          "levels": "Normal"
        },
        "temperature": {
          "value": 100,
          "levels": "Normal"
        }
      }
    ],
    "diagnostic_list": [
      {
        "name": "Type 2 Diabetes",
        "description": "A chronic condition that affects the way the body processes blood sugar (glucose).",
        "status": "Actively being treated"
      },
      {
        "name": "Type 2 Diabetes",
        "description": "A chronic condition that affects the way the body processes blood sugar (glucose).",
        "status": "Untreated"
      },
      {
        "name": "Hypertension",
        "description": "A condition in which the force of the blood against the artery walls is too high.",
        "status": "Under observation"
      }
    ],
    "lab_results": [
      "Complete Blood Count (CBC)",
      "Echocardiogram",
      "Liver Function Tests",
      "Mammography",
      "Urinalysis",
      "Ultrasound",
      "Prostate-Specific Antigen (PSA)",
      "Hemoglobin A1C",
      "Lipid Panel",
      "Radiology Report"
    ]
  },
 */