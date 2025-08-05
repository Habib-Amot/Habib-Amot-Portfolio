import React from 'react'
import { SlArrowLeftCircle } from "react-icons/sl";
import { SlArrowRightCircle } from "react-icons/sl";
import { MdOutlineError } from "react-icons/md";

import './styles.css'

const ImageSlider = ({url, limit}) => {
  let [currentImageIndex, setCurrentImageIndex] = React.useState(0);
  let [images, setImages] = React.useState([]);
  let [isLoading, setIsLoading] = React.useState(true);
  let [error, setError] = React.useState(null);

    async function fetchImages(url) {
      console.log(url)
      try {
        setIsLoading(true);
        const response = await fetch(url);
        if(!response.ok){
          setError('Unable to load images from source');
          setIsLoading(false);
        }
        let imageData = await response.json()
        if(imageData) setImages(imageData);
        else setError("unable to load images")
        setIsLoading(false)
      }catch(e){
        setError(e.message);
        setIsLoading(false);
      }
    }
    
  React.useEffect(() => {
    fetchImages(url+'?limit='+limit);
  }, [url, limit])

  let data = null;
  if (isLoading){
    data = <div className='spin'></div>
  }
  else if (error){
    data = <div className='error'><MdOutlineError/>{error}</div>
  }
  else if(images.length > 0){
    data = <div className='images'>{images.map(image => {
      return (
        <img src={image.download_url} alt={image.author} key={image.id} className={image.id == currentImageIndex ? 'selected':'not-selected'}/>
      )
    })}
    </div>
  }

  function handlePrev(){
    if(currentImageIndex == 0){
      setCurrentImageIndex(images.length - 1);
    }else{
      setCurrentImageIndex(currentImageIndex - 1);
    }
  }

  function handleNext(){
    if(currentImageIndex == images.length - 1){
      setCurrentImageIndex(0);
    }else{
      setCurrentImageIndex(currentImageIndex + 1);
    }
  }
  return (
    <div>
      <h1>Image Slider</h1>
      <div className='slider-container'>
        <button className='btn prev' onClick={handlePrev}><SlArrowLeftCircle/></button>
        {data}
        <button className='btn next' onClick={handleNext}><SlArrowRightCircle/></button>
        {images && images.length > 0 ? <div className='indicators'>
          {images.map((_, index)=>
            <span key={index} onClick={()=>setCurrentImageIndex(index)} className={currentImageIndex == index ? 'indicator current': 'indicator'}>

            </span>
          )}
        </div>:null}
      </div>
    </div>
  )
}

export default ImageSlider
