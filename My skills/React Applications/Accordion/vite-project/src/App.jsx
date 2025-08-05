import accordion from './data'
import { useState } from 'react';
import './App.css'

function App() {
  let [selected, setSelected] = useState(null);
  let [multipleAccordion, setMultipleAccordion] = useState([]);
  let [selectMultiple, setSelectMultiple] = useState(false);

  function toggleAccordion(index) {
    if (selectMultiple) {
      if (multipleAccordion.indexOf(index) === -1) {
        let newMultipleAccordion = [...multipleAccordion, index];
        setMultipleAccordion(newMultipleAccordion);
      }else{
        let newMultipleAccordion = multipleAccordion.filter((item) => item !== index);
        setMultipleAccordion(newMultipleAccordion);   
      }
    }else{
      if (selected === index) {
        setSelected(null);
      } else {
        setSelected(index);
      }
    }
  }

  return (
    <div className="App">
      <button className="btn" onClick={() => setSelectMultiple(!selectMultiple)}>
        {selectMultiple ? "Disable Multiple Selection" : "Enable Multiple Selection"}
      </button>
      <h1>Accordion Component</h1>
      <p>This is a simple accordion component built with React. It allows you to expand and collapse sections of content.</p>
      <p>Click on the headers to expand or collapse the content.</p>
      {accordion && accordion.length > 0 ? <div className="accordion">
          {accordion.map((item) => 
            <div className="accordion-item" key={item.id} onClick={() => toggleAccordion(item.id)}>
              <div className="accordion-header">
                <h3>{item.title}</h3> 
                <span>{selected == item.id || multipleAccordion.indexOf(item.id) != -1 ? "-" : "+"}</span>
              </div>
              <div className="accordion-content">
                {selected == item.id || multipleAccordion.indexOf(item.id) != -1 ? <p>{item.content}</p> : null}
              </div>
            </div>)
          }
        </div> : <div className="no-data">
          <h2>No data available</h2>
          <p>Please check your data source or try again later.</p>
          <p>If you are using a local JSON file, make sure it is in the correct format and accessible.</p>        
        </div>}
    </div>
  )
}

export default App
