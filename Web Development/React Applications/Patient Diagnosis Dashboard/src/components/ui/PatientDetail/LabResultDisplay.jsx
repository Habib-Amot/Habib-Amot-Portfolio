import downloadIcon from '../../../assets/icons/downloadIcon.svg'

const LabResultDisplay = ({resultName}) => {
  return (
    <div className='flex items-center justify-between w-full'>
      <p className="capitalize flex items-center h-full text-sm">
        {resultName} 
      </p>
      <img src={downloadIcon} alt="" className="w-4 h-4 font-black"/>
    </div>
  )
}

export default LabResultDisplay
