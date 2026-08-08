import { useState } from 'react'
import './App.css'
import { FaStar } from 'react-icons/fa';

function App() {
  let [backgroundColor, setBackgroundColor] = useState("#ffffff");

  function generateHexColor(){
    let hexDigits = [
      '1', '2','3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'
    ]
    let color = '';
    for(let number=0; number < 6; number++){
      color += hexDigits[Math.floor(Math.random() * hexDigits.length)]
    }
    return "#"+color;
  }

  function generateRGBColor(){
    let rgbList = [];
    let rgbColor = "";
    for(let number=0; number < 3; number++){
      rgbList.push((Math.floor(Math.random() * 255)).toString())
    }
    rgbColor = rgbList.join(',');
    return `rgb(${rgbColor})`
  }

  function generateRandomColor(){
    let bgColors = [generateHexColor(), generateRGBColor()]
    return bgColors[Math.floor(Math.random() * 2)]
  }

  return (
    <div className="App" style={{backgroundColor:backgroundColor}}>
      <div className='btns'>
        <button onClick={()=>{setBackgroundColor(generateHexColor)}}>Generate Hex Color</button>
        <button onClick={()=>{setBackgroundColor(generateRGBColor)}}>Generate RGB Color</button>
        <button onClick={()=>{setBackgroundColor(generateRandomColor)}}>Generate Random Color</button>
        <FaStar className='star active' size={12} color="black" count={10} style={{color:"brown"}}/>
      </div>
      <div className='color'>
        {backgroundColor}
      </div>
      
    </div>
  )
}

export default App
