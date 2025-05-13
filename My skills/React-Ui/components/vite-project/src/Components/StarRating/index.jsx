import React, { useState } from 'react'
import { FaStar } from 'react-icons/fa';

const Rating = ({starCount = 5}) => {
    let [rating, setRating] = useState(0);
    let [hover, setHover] = useState(0);

    let indexArray = Array.from(Array(starCount).keys()).map(item => item+1);
    
  return (
    <div className='rating'>
      {indexArray.map(index => <FaStar key={index} size={16} className={(hover || rating) >= index ? 'star' : 'white'}
        onMouseEnter={()=>{setHover(index)}} 
        onMouseLeave={()=>{setHover(0)}}
        onClick={()=>{setRating(index)}}
       />)}
       <p>{hover || rating} Star{(hover || rating) > 1 ? 's' : null} Rating</p>
    </div>
  )
}

export default Rating
