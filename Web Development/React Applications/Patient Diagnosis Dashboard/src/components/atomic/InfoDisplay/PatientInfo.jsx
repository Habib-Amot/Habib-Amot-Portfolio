const PatientInfo = ({ico, header, value}) => {
  return (
    <div>
      <div className="flex gap-4 items-center w-full h-auto justify-start">
        <div className="ico *:w-6 *:h-6 bg-gray-400 overflow-hidden rounded-full flex items-center justify-center">
            <img src={ico} alt="" className="w-full h-full"/>
        </div>
        <div className="flex flex-col gap-1 items-start justify-center">
            <h4 className="text-sm font-normal capitalize">{header}</h4>
            <p className="text-xs font-extrabold capitalize">{value}</p>
        </div>
      </div>
    </div>
  )
}

export default PatientInfo
