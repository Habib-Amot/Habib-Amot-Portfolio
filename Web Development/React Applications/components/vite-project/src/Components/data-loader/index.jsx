import { useState, useEffect } from 'react';

const DataLoader = () => {
    let [data, setData] = useState([]);
    let [loading, setLoading] = useState(false);
    let [dataCount, setDataCount] = useState(0);
    let [error, setError] = useState(null);

    async function fetchData(url) {
        setLoading(true);
        try{
            let response = await fetch(url);
            let data = await response.json();
            setData(data['products']);
            console.log(data)
            setDataCount(data.length);
            setLoading(false);
        
        }catch(e){
            setLoading(false)
            setError(e.message)
        }
    }

    useEffect(() => {
        fetchData(`https://dummyjson.com/products?limit=10&skip=${dataCount}&select=title,price,thumbnail,description`);
    }, [dataCount])

    let dataComponent;
    if(loading){
        dataComponent = <p>Please wait...Loading Data </p>
    }
    else if(error){
        dataComponent = <p>Error: {error}</p>
    }
    else if(data && data.length > 0){
        console.log(555)
        dataComponent = (
            <div>
                {data.map((item, index)=> 
                    <div key={index}>
                        <h2>{item.title}</h2>
                        <img src={item.image} alt={item.title} />
                        <p>{item.description}</p>
                    </div>
                )}
            </div>
        )
    }
  return (
    <div>
      <h1>Dataloader component</h1>
      {dataComponent}
    </div>
  )
}

export default DataLoader
