
const BloodPressureDetailItem = ({icon, readingName, readingValue, readingLevel, bgColor, reading_unit}) => {
  return (
    <div className="p-4 flex flex-col gap-2 h-52 w-49 rounded-xl" style={{backgroundColor: bgColor}}>
        <div className="ico">
            <img src={icon} alt="reading image" />
        </div>
        <div className="readings">
            <h2 className="font-medium text-xs">{readingName}</h2>
            <p className="text-2xl font-black">{readingValue} {reading_unit}</p>
        </div>
        <p className="text-xs">{readingLevel}</p>
      
    </div>
  )
}

export default BloodPressureDetailItem
