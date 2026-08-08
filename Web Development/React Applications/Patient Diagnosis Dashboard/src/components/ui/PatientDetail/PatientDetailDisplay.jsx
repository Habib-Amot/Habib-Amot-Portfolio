const PatientDetailDisplay = ({name, description, status}) => {
    let detail = [name, description, status]
  return (
    <div className="grid grid-cols-[1.5fr_2fr_1fr] auto-rows-12 text-xs w-full h-10 px-3">
      {
        [0, 1, 2].map( _ => <p key={_} className="capitalize flex items-center h-full w-full">{detail[_]}</p>)
      }
    </div>
  )
}

export default PatientDetailDisplay
