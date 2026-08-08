import accordion from './data'
import { useState } from 'react';
import './App.css'

export default function App() {
    let [selected, setSelected] = useState(null);
    let [multipleAccordion, setMultipleAccordion] = useState([]);
    let [enableMultiple, setEnableMultiple] = useState(false)


    function handleSelected(index){
        if(enableMultiple){
            if(multipleAccordion.indexOf(index) == -1){
                let newMultiple = [...multipleAccordion, index];
                setMultipleAccordion(newMultiple)
            }else{
                setMultipleAccordion(multipleAccordion.filter((item) => item !== index))

            }
        }else{
            selected == index ? setSelected(null) : setSelected(index)
        }
    }
    return (
        <div className="App">
            <div className='accordion-header'>
                <h1>Simple Accordion</h1>
                <p>This is a simple accordion component built with React. It allows you to expand and collapse sections of content.</p>
                <small>Click on the headers to expand or collapse the content.</small>
            </div>
            <button onClick={()=>{setEnableMultiple(!enableMultiple)}}>
                {enableMultiple ? "Disable Multiple Selection" : "Enable Multiple Selection"} 
            </button>
            {accordion && accordion.length > 0 ? <div className='accordion'>
                {accordion.map((item) => 
                    <div className='accordion-item' key={item.id} onClick={()=> handleSelected(item.id)}>
                        <div className='accordion-header'>
                            <h3>{item.title}</h3>
                            <span>{multipleAccordion.indexOf(item.id) !== -1 || item.id == selected ? "-" : "+"}</span>
                        </div>
                        <div className='accordion-content'>
                            {multipleAccordion.indexOf(item.id) !== -1 || item.id == selected ? item.content : null}
                        </div>
                    </div>
                )}
                </div>
            : <div className='no-data'>
                <h2>No data available to display</h2>
            </div>}
        </div>
    )
}
