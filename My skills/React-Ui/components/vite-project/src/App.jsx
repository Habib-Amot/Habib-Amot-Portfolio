import './App.css'
import Rating from './Components/StarRating'
import ImageSlider from './Components/ImageSlider'
import DataLoader from './Components/data-loader'

function App() {

  return (
    <>
       <Rating starCount={10}/>
       <ImageSlider url= 'https://picsum.photos/v2/list' limit={6}/>
       <DataLoader limit={25}/>
    </>
  )
}

export default App
